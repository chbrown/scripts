#!/usr/bin/env node
'use strict'; /*jslint node: true, es5: true, indent: 2 */
var fs = require('fs');
var marked = require('marked');
var child_process = require('child_process');

// marked.setOptions({});

var optimist = require('optimist')
  .usage('md doc.md')
  .describe({
    input: 'Markdown input',
    output: 'HTML output',
    head: 'Header HTML',
    help: 'print this help message',
  })
  .boolean(['help'])
  .default({
    // input: '*.md',
    head: '~/.standardhead.html',
  });

var argv = optimist.argv;

var md_extension = function(file) { return file.match(/.md$/); };

if (argv.help) {
  optimist.showHelp();
}
else {
  var input_filepath = argv._[0] || argv.input || fs.readdirSync('.').filter(md_extension)[0];
  var input_markdown = fs.readFileSync(input_filepath, {encoding: 'utf8'});
  marked(input_markdown, {}, function(err, input_html) {
    if (err) throw err;

    var head_filepath = argv.head.replace(/^~/, process.env.HOME);
    var head_html = fs.readFileSync(head_filepath, {encoding: 'utf8'});

    var output_filepath = input_filepath.replace(/md$/, 'html');
    fs.writeFileSync(output_filepath, head_html + input_html, {encoding: 'utf8'});
    console.log('Wrote html to %s', output_filepath);

    child_process.exec('open ' + output_filepath, function(err, stdout, stderr) {
      if (err) throw err;
      console.log('Opened %s', output_filepath);
    });
  });
}
