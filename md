#!/usr/bin/env node
/*jslint node: true */
var fs = require('fs');
var path = require('path');
var marked = require('marked');
var streaming = require('streaming');
var child_process = require('child_process');

var optimist = require('optimist')
  .usage([
    'Usage: md README.md README.html',
    '       md <README.md >README.html',
    '',
    'Render Markdown to html, prefixing it with an HTML header.',
    '',
    'If the first argument is specified and is not "-", md reads input from',
    'that path. Otherwise, md reads from stdin.',
    'If the second argument is specified and is not "-", md writes output to',
    'that path. Otherwise, md writes to stdout.',
    'The contents of ~/.standardhead.html, if it exists, will be prepended to',
    'the HTML output.'
  ].join('\n'))
  .describe({
    head: 'Header HTML',
    help: 'print this help message',
  })
  .boolean(['help'])
  .default({
    head: path.join(process.env.HOME, '.standardhead.html'),
  });

function render(input_stream, output_stream, callback) {
  streaming.readToEnd(input_stream, function(err, chunks) {
    if (err) return callback(err);

    var input_markdown = Buffer.concat(chunks).toString('utf8');
    marked(input_markdown, {}, function(err, input_html) {
      if (err) return callback(err);

      var head_stream = fs.createReadStream(argv.head);
      head_stream.pipe(output_stream, {end: false});
      head_stream.on('end', function() {
        output_stream.write(input_html);
        callback();
      });
    });
  });
}

if (require.main == module) {
  var argv = optimist.argv;

  if (argv.help) {
    optimist.showHelp();
    process.exit(0);
  }

  var arg_in = argv._[0];
  var arg_out = argv._[1];

  var done = function(err) {
    if (err) throw err;
  };

  var input_stream = null;
  var output_stream = null;
  if (!process.stdin.isTTY || arg_in == '-') {
    input_stream = process.stdin;
  }
  else if (arg_in) {
    var input_filepath = arg_in;
    input_stream = fs.createReadStream(input_filepath);
  }
  else {
    throw new Error('You must specify some Markdown input');
  }

  if (arg_out && arg_out != '-') {
    var output_filepath = arg_out;
    output_stream = fs.createWriteStream(output_filepath);

    done = function(err) {
      if (err) throw err;
      child_process.exec('open ' + output_filepath, function(err, stdout, stderr) {
        if (err) throw err;
        output_stream.end();
        console.log('opened %s', output_filepath);
      });
    };
  }
  else {
    output_stream = process.stdout;
  }

  render(input_stream, output_stream, done);
}
