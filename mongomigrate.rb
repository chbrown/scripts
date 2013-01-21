#!/usr/bin/env ruby
# gem install net-ssh net-scp
require 'net/ssh'
require 'net/scp'
require 'optparse'

class MongoDatabase
  attr_accessor :host, :db, :local
  def initialize(str)
    parts = str.split(':')
    @host, @db = if parts.length == 1
      ['localhost', parts[0]]
    else
      parts
    end
    @local = @host == 'localhost'
  end

  def to_s
    "#{host}:#{db} (#{local ? 'LOCAL' : 'REMOTE'})"
  end
end

abort("Usage: mongomigrate.rb asl:drags localhost:drags") if ARGV.length != 2

source = MongoDatabase.new(ARGV[0])
destination = MongoDatabase.new(ARGV[1])
destination.db = source.db if !destination.db

puts "#{source} -> #{destination}"

tmp_dir = "/tmp/mongo"

# transfer from local (source) to remote (destination)
remote, local = destination.local ? [source, destination] : [destination, source]
Net::SSH.start(remote.host, 'chbrown') do |ssh|
  db_common = "#{remote.db}-#{local.db}"
  puts "# Using #{db_common} as the common db folder name"

  puts '# Clean up tmp on remote'
  puts ssh.exec! "rm -rf #{tmp_dir}/#{db_common}_dump"
  puts ssh.exec! "mkdir -p #{tmp_dir}/#{db_common}_dump" # may produce error
  puts ssh.exec! "rm #{tmp_dir}/#{db_common}.tgz" # may produce error
  puts '# Clean up tmp locally'
  puts %x[rm -rf #{tmp_dir}/#{db_common}_dump] # may produce error
  puts %x[mkdir -p #{tmp_dir}/#{db_common}_dump]
  puts %x[rm #{tmp_dir}/#{db_common}] # may produce error

  if remote == source
    puts '# Package up on the remote side'
    puts ssh.exec! "mongodump --db #{remote.db} --out #{tmp_dir}/#{db_common}_dump"
    puts ssh.exec! "cd #{tmp_dir} && tar -czf #{db_common}.tgz #{db_common}_dump"
    puts '# Pull down tarball from remote to local, courtesy NET::SCP'
    ssh.scp.download! "#{tmp_dir}/#{db_common}.tgz", "#{tmp_dir}/#{db_common}.tgz"
    puts '# Import locally'
    puts %x[cd #{tmp_dir} && tar -xzf #{tmp_dir}/#{db_common}.tgz]
    puts %x[mongorestore --db #{local.db} #{tmp_dir}/#{db_common}_dump/#{remote.db}]
  else
    puts '# Package up locally'
    puts %x[mongodump --db #{local.db} --out #{tmp_dir}/#{db_common}_dump]
    puts %x[cd #{tmp_dir} && tar -czf #{db_common}.tgz #{db_common}_dump]
    puts '# Push tarball from local to remote'
    puts "$ scp #{local.host}:#{tmp_dir}/#{db_common}.tgz #{remote.host}:#{tmp_dir}/#{db_common}.tgz"
    ssh.scp.upload! "#{tmp_dir}/#{db_common}.tgz", "#{tmp_dir}/#{db_common}.tgz"
    puts '# Import on the remote machine'
    puts ssh.exec! "cd #{tmp_dir} && tar -xzf #{tmp_dir}/#{db_common}.tgz"
    puts ssh.exec! "mongorestore --db #{remote.db} #{tmp_dir}/#{db_common}_dump/#{local.db}"
  end
end
