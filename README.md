# scripts

Some handy short scripts I like, many of which I've written all by myself!

## Installation

```bash
cd ~
git clone git://github.com/chbrown/scripts.git
echo 'export PATH=$HOME/scripts:$PATH' >> .bashrc.local
```

Prerequisite for many of these scripts:

```bash
easy_install requests colorama chardet jinja2 PyYAML
```

## License

Copyright © 2012–2013 Christopher Brown. [MIT Licensed](LICENSE).

Except for following files, I am the sole author of all of these scripts.

* `htpasswd.py`
* `otf2ttf2eot.sh`
* `transpose`
* `lib/` and everything in this directory.

---

# active

Remove inactive lines; i.e., lines that are empty, whitespace-only, or comments.
Comments are where the first non-whitespace character/string is `#`, `//`, or `--`.

    cat /etc/hosts | active

It uses a `sed -f` shebang, so, alternatively:

    active /etc/hosts

# alphadec

Create 10 alphadecimal passwords of length 16 each.

    alphadec --length 16 --count 10


# bow

Tabulate bags of words from text supplied on STDIN. Each input line is treated
as a distinct document and split on whitespace. Prints out each bag of words in
type:number format, most common first (ordering for types with same total count
is undefined).

    echo 'the dog bit the man who pet the other dog' | bow

> the:3 dog:2 other:1 who:1 bit:1 man:1 pet:1


# crawl

A shortcut to this `wget` sequence:

    wget -e robots=off --recursive --no-clobber --page-requisites --convert-links --restrict-file-names=windows $1


# csv2html

E.g.,

    csv2html batch_results.csv > batch_results.csv.html

# csv2tsv

Uses Python's dialects to convert.

    cat sb5b.csv | tr '\r' '\n' | csv2tsv > sb5b.tsv

# curlweb2.0

Wait until a page doesn't scroll down anymore, and then output the DOM to `STDOUT`.

    curlweb2.0 http://animalstalkinginallcaps.tumblr.com/

# doi

Download BibTeX using [CrossRef's](https://www.crossref.org/) [content negotiation functionality](https://www.crossref.org/blog/content-negotiation-for-crossref-dois/), then reformat with [bartleby](https://github.com/chbrown/bartleby).

    doi 10.1109/5.771073

# drop

Drop (delete) the first line (or `n` lines, if `n` is specified) of `/dev/stdin`.

    ls -l | drop
    ls -la | drop 3

# fit

One-liner for when you have some lengthy lines and you want to kill the wrap:

    tr '\t' ' ' | cut -c -$(tput cols)

# grephistory

Case-insensitively `grep` through `~/.bash_history`.
All arguments are combined into a single string.

    grephistory lein run

# groupby-sum

Given whitespace-separated input on STDIN with lines like `<value>\t<count>`, group by unique values and sum the counts for each group. Example:

    $ groupby-sum <<EOF
    a 10
    b 1
    a 20
    a 30
    b 2
    a 40
    EOF

Output:

    a   100
    b   3

# htpasswd.py

Script originally from a guy named "Eli Carter."

After `alphadec`'ing a password, say, `vsw8lq4NuM0S`, create an `htpasswd` file called `nginx.htpasswd` with that password for the user `scriptuser`. I think it adds to an existing file if `nginx.htpasswd` already exists.

    htpasswd.py -c -b nginx.htpasswd scriptuser vsw8lq4NuM0S

# intersect

Collect the lines that all specified files share:

    intersect users-extant.txt users-needtodelete.txt > todo.txt

Each file is `uniq`ed, trailing whitespace is discarded, and output order is unspecified.

# jinja

Simple wrapper around [jinja2](http://jinja.pocoo.org/docs/) to render a common template with variable input.
Not sure why the `jinja2` package doesn't provide this, at least as a `python -m ...` call.

Input can be specified as a filename, but defaults to STDIN.
It can be in either JSON or YAML format.

One-line example:

    jinja <(echo 'hello {{name}}') <<<'{"name":"world"}'
    #=> hello world

File-based example:

`email.jinja.md` contents:

    # {{ subject.title() }} from {{ from }}

    Sent to:
    {% for recipient in [to] + cc %}
    * {{ recipient }}
    {% endfor %}

    Body:
    > {{ body }}

`email.json` contents:

    {
        "subject": "Greetings!",
        "from": "@chbrown",
        "to": "supervisor@lesspress.net",
        "cc": ["lefty@other.com", "gels@schenectady.org"],
        "body": "Hey lemme know if you got this..."
    }

Running `cat email.json | jinja email.jinja.md` produces the following:

    # Greetings! from @chbrown

    Sent to:
    * supervisor@lesspress.net
    * lefty@other.com
    * gels@schenectady.org

    Body:
    > Hey lemme know if you got this...

# jqi

`jqi` is `jq` `i`n-place.

Call [`jq`](http://stedolan.github.io/jq/) and overwrite the input with the output.

For example, to pretty-print a JSON file in-place:

    jqi . search-result.json

It uses the last command line argument as the file that it will overwrite, so it only really makes sense to have one input file.

If it encounters any errors, it prints the temporary and backup filepaths it uses to `stderr`.

# jsmap

When [`jq`](http://stedolan.github.io/jq/) isn't enough (it usually is), this is like `perl -e` but for `node` (and JSON).

1. Input newline-separated JSON on `stdin`.
2. The first command line argument is the program code.
3. The input object is available as `$in`.
4. The transformation should set as `$out`,
5. ...which will be `JSON.stringify`'d
6. ...and sent to `stdout` (as newline-separated JSON).

For example:

    jsmap '$out = {id: $in.id}'

Is equivalent to:

    jq '{id: .id}'

If you want to run a stream of JSON through a file without having to handle the JSON conversion on each side, try [jsed](https://github.com/chbrown/jsed), which was spun out of this script.

# launch

Simply grep for a Mac LaunchAgent that matches the given argument, and start it. Easy way to have databases around but not always use them when not developing.

    launch redis
    > launchctl start homebrew.mxcl.redis

It found the LaunchAgent called homebrew.mxcl.redis and started it.

# launcrm

Basically undo what `launch` does.

    launchrm mongo

# lsmcat

Given a bunch of plain text files, concatenate them all, tranforming each into the format:

    [File creation date in ISO format] Filename.txt

    <File contents>

So, if you have a folder of iPad notes, say, simply do something like:

    cd ~/Dropbox/ipad-notes
    lsmcat Ideas/*.txt > Ideas.txt
    rm -r Ideas/
    cat Ideas.txt

# mac.py

Display your current MAC address:

    mac.py --display

Generate a random valid MAC address:

    mac.py --gen

Reset your current MAC address to a random new one:

    sudo mac.py


# md5py

MD5-hash each of the command line arguments.

    md5py freshplum

_N.b._: If given a filename, this doesn't sum the file, but the filename!

# nargs

One-line bash script to print out the number of arguments passed in.
Useful for debugging variables and variable expansion.

    nargs "Just two" arguments
    > 2

# openssl-showcerts

Use `openssl` to retrieve and print information about the SSL/TLS certificate(s) offered by a server on the internet.

    openssl-showcerts serverfault.com

# otf2ttf2eot.sh

Convert an OTF font file to EOT with fontforge

    otf2ttf2eot.sh TimesNewRoman.otf

# path2name

Convert a filepath into a flat filename.

    ls -d ~/.bashrc | path2name
    #=> home-dot_bashrc

    ls -d /tmp/server.log | path2name
    #=> root-tmp-server.log

    ls -d Music/Audiobooks | path2name
    #=> Music-Audiobooks

| Replaces this                        | with this |
|-------------------------------------:|:----------|
| hidden-file dots                     | `dot_`    |
| `~/`                                 | `home-`   |
| leading `/`                          | `root-`   |
| other `/` separators                 | `-`       |
| any non-portable filename characters | `-`       |

# pcol

Like `col`, but auto-adjusts with more text. Slower, obviously.

    cat ANEW2010All.txt | pcol -s \\t

## `pof` (bash)

Lists all file descriptors open by the current shell, excluding regular files.

Simply runs: `lsof -p $$ | grep -v REG`


## `pg_backup` (bash)

Pipes `pg_dump` though `bzip2` and saves an ISO 8601-timestamped file (`YYYYMMDD-<name>.sql.bz2`) in the current directory. If such a file already exists, it will also use the time part of the date (`YYYYMMDDThhmmss-<name>.sql.bz2`).

    pg_backup flickr

Outputs:

    Dumping PostgreSQL database 'flickr' to '20150130-flickr.sql.bz2'

Running the same command again will see the file conflict and avoid clobbering the original:

    Dumping PostgreSQL database 'flickr' to '20150130T153636-flickr.sql.bz2'


## `pg_migrate` (python)

Copy a complete PostgreSQL database from one host to another (or to the same host under a different database name).
Supports remote hosts via ssh.

    pg_migrate -cd dark:twitter_dev localhost:twitter_dev

Uses python to construct a `ssh -C` and `pg_dump` pipeline. Options:

* `-d` / `--drop` runs `dropdb` on the target host as needed.
* `-c` / `--create` runs `createdb` on the target host.


# ppxml

Pretty print XML using [Libxml](http://xmlsoft.org/)'s [`xmllint`](http://xmlsoft.org/xmllint.html) tool.

    ppxml APW19980322.0749.tml

# prefix

Prefix file(s) with a literal string or timestamp, in the latter case, the birthtime of the specified file(s).

    prefix ExportArticle.pdf

Supposing `ExportArticle.pdf` was created on 2016-04-11, this moves `ExportArticle.pdf` to `20160411-ExportArticle.pdf`.

If the target destination exists, `prefix` exits with an error. See `prefix --help` for more options.

# prependbom

Prepend the UTF-8 byte order marker (BOM) to the input. Uses `fileinput`, so STDIN and all files supplied as command line arguments will be streamed to STDOUT after the BOM byte sequence, `\xef\xbb\xbf`.

    <flat.txt prependbom > flat.utf8

# redis-del

Do a combo redis KEYS "prefix:*" command and then DEL whatever it finds.

    redis-del domains:*

# redismigrate

Needs to be generalized. Currently copies everything from a hard-coded remote host, "dark", (over automatically opened SSH tunnel) to localhost, using the hard-coded in "forex:*" key wildcard.

    redismigrate

But you get the idea.

# rmfile

`rmfile` is like the standard POSIX `rmdir`, but for files—it only deletes a file if the file is empty.

    $ touch blank.txt
    $ rmfile blank.txt
                                        # no output, indicating success
    $ mkdir subdir
    $ rmfile subdir
    rmfile: subdir: Not a file

    $ echo 'hello world' > hello.txt
    $ rmfile hello.txt
    rmfile: hello.txt: File not empty

    $ rmfile nothere.txt
    rmfile: nothere.txt: No such file or directory


Also serves as a pretty good example for writing a script with POSIX-like error messages, exit codes, and output.

# sf

Little helper for the awesome `sshfs` tool that OS X Fuse provides. It'll make the given directory as needed, and die quietly if the connection already exists.

    sf tacc: /Volumes/tacc

# smv

Secure move. Like scp but remove the files after copying.

    smv 2013-09-07.json.gz 2013-09-08.json.gz /mnt/backup/days_and_days --delete

# stopwatch

Basic duration timer.

    stopwatch
    > Press \n to end.
    ↪
    > 1.3509s

# ssh-copy-rsa

Just cat current user's `id_rsa.pub` into remote `.ssh` directory on the given server, creating `.ssh` and `authorized_keys2` if necessary:

    ssh-copy-rsa dark

You may need to fix the permissions on the remote's new `~/.ssh`, i.e.:

    700 .ssh
    644 .ssh/authorized_keys2

# style

Recursively check files in the specified directories for trailing whitespace and zero/multiple newlines at EOF.

    style ~/github/

Add `--fix` to automatically remove the misplaced whitespace (in place, no backups).

This can be destructive since it recurses over all files, including binaries; it might be wise to specify exactly which files when using `--fix`:

    style --fix ~/github/**/*.py

# stmux

SSH into a remote server and start or resume the tmux session there, using the iTerm v3 integration:

    stmux dark

Uses the session name "0", which is the default when starting a new tmux session.

# tabs2spaces

Replace tabs with character padding sufficient to fit all values in a given column. Reads entire stdin before outputting anything in order to measure the width of each column.

    tabs2spaces < accounts.tsv


# tabulate

Like `sort | uniq -c | sort -g`, but with nice formatting. E.g.,

    </usr/share/dict/words cut -c -1 | tabulate --format markdown

Outputs this:

    | count | value |
    |------:|:------|
    |    77 | Q     |
    |    92 | X     |
    |   139 | Y     |
    |   208 | U     |
    ... only a snippet shown here ...
    | 14537 | a     |
    | 16179 | u     |
    | 17406 | c     |
    | 22171 | p     |
    | 22759 | s     |

Which renders into this:

| count | value |
|------:|:------|
|    77 | Q     |
|    92 | X     |
|   139 | Y     |
|   208 | U     |
|   ... | ...   |
| 14537 | a     |
| 16179 | u     |
| 17406 | c     |
| 22171 | p     |
| 22759 | s     |

# tnls

List all active ssh tunnels, looking for something like `ssh ... -L ...`.

# tjz

Run `tar cj` and move the original into `/tmp`:

    $ tjz table_extractor/
    created table_extractor.tar.bz2 and moved original to /tmp/table_extractor-20160117T135651

It will exit gracefully if the original does not exist, or if the target `$1.tar.bz2` file already exists.

# total

Sum all numbers given on stdin, separated by any kind of whitespace.

Uses `tr`, `paste`, and `printf` to format the input into an equation format.

Then runs `bc` ("An arbitrary precision calculator language") to compute the sum.

    printf "1\n2 3\n4 5 6" | total

# transpose

Super-complicated Awk script for transposing like in Excel.

    transpose alice-results.dat | pcol -g 2

# triage

List the total sizes of the specified directories' children nodes, in Megabytes, sorted from smallest to largest.

    triage Desktop Music Downloads

Without arguments, defaults to the current directory, as if calling `triage .`

# vsplitimg

Open all files in the current folder as images, split them into half, left and right, (like opening a normal book), and save as the original filenames suffixed with `-left` or `-right`, JPEGs with quality 95.

    cd ~/Pictures/scans
    vsplitimg *.jpg

Requires `PIL`: `brew install PIL` or `pip install -U PIL` if you're feeling optimistic

# wgetar

`wget + tar -x` helper. Usage:

    wgetar URL [TARGET] [-v|--verbose] [-h|--help]

Use `wget` to download a tarball from `URL` and streamingly extract the contents into the `TARGET` directory
(which defaults to the basename of `URL` without the `.tar.*` or `.t*` extension),
decompressing based on the extension. E.g.:

    wgetar http://ftp.gnu.org/gnu/wget/wget-1.5.3.tar.gz

The supported extensions are `.tar.gz|.tgz`, `.tar.bz2|.tbz2|.tbz`, `.tar.xz|.txz`, and `.tar.lzma|.tlzma`.

# zipf

Print out the most common words in a plain text document.

    cd ~/corpora/heliohost
    <Fre_Newspapers.txt zipf
