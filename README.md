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

* `autoreload`
* `htpasswd.py`
* `otf2ttf2eot.sh`
* `transpose`
* `lib/` and everything in this directory.

---

# alphadec

Create 10 alphadecimal passwords of length 16 each.

    alphadec --length 16 --count 10


# autoreload

Watch a directory for changed files and restart a process when a change is detected.

    autoreload python main.py

From [stevekrenzel/autoreload](https://github.com/stevekrenzel/autoreload) (no license).

# bow

Tabulate bags of words from text supplied on STDIN. Each input line is treated
as a distinct document and split on whitespace. Prints out each bag of words in
type:number format, most common first (ordering for types with same total count
is undefined).

    echo 'the dog bit the man who pet the other dog' | bow

> the:3 dog:2 other:1 who:1 bit:1 man:1 pet:1


# click

Measured from the top left of the screen, left-click once.

    click -x 600 -y 400


# cfmt

Beautify all source code in `./src/*.c` and `./src/*.h`, in-place.

Uses [`astyle`](http://astyle.sourceforge.net/) with the following options:

    astyle
       --style=java
       --
       --unpad-paren
       --delete-empty-lines
       --add-brackets
       --convert-tabs
       --align-pointer=type
       --lineend=linux
       --suffix=none $file

Get `astyle` from your package manager, e.g.:

    brew install astyle


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

# gh

Open any [GitHub](https://github.com/) pages which the current git repo has as remotes.

    cd ~/scripts
    gh # opens https://github.com/chbrown/scripts in your browser

# gscat

Short wrapper around the Ghostscript command, `gs`, that simply reads in a PDF and outputs the same PDF with the extension `.gs.pdf` instead of `.pdf`. This is useful with large PDFs, or copy-protected PDFs, etc., where you just want a plain, simple, efficient, no-nonsense PDF to work from.

    gscat High-res-proofs.pdf

# fit

One-liner for when you have some lengthy lines and you want to kill the wrap:

    tr '\t' ' ' | cut -c -$(tput cols)

# fixpdf

Wrapper around `gs` command with reasonable options.

    fixpdf Bulky.pdf

> fixpdf: wrote gs output to Bulky-gs.pdf

Writes to the path specified by the second argument,
or appends `-gs` to the basename of the first argument if no other arguments are supplied.

# git-remote-tags

Wrapping around `git ls-remote --tags git://...` to get the good stuff:

    git-remote-tags chbrown/amulet

Assumes github.

# git-submodule-rm

Until git 1.8.3 rolls around:

    git-submodule-rm static/lib

Thanks goes to [stackoverflow](http://stackoverflow.com/questions/1260748/how-do-i-remove-a-git-submodule).

# github-api

Simple request and printing helper for the Github API v3 (automatically pulls in `$GITHUB_TOKEN` environment variable).

    github-api /user
    github-api /user/emails
    github-api /user/issues
    github-api /users/isaacs
    github-api /orgs/utcompling/members
    github-api /repos/chbrown/flickr-with-oauth/events | json

Not yet supported:

    github-api /repos/chbrown/flickr-with-oauth/issues state=closed

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

Input can be specifed as a filename, but defaults to STDIN.
It can be in either JSON or YAML format.

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

# json2yaml

YAML is a superset of JSON, so there are lots of ways to convert JSON to YAML. I say, one is better than none.

    json2yaml < package.json
    > name: scripts
    > version: 0.2.0
    > description: Handy scripts
    > keywords:
    >   - scripts
    > ...

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


## `md` (node.js)

Convert Markdown to HTML and prefix with a global header.

    md README.md README.html

Or you can pipe Markdown into `md`. The example below dumps the HTML to a temporary file and opens it in Firefox.

    pbpaste | md > /tmp/pasteboard.html
    open -a Firefox.app /tmp/pasteboard.html

The header filepath defaults to `~/.standardhead.html`.


# md5py

MD5 hash the last command line argument.

    md5py freshplum

_N.b._: If given a filename, this doesn't sum a file, but the filename!

# mongomigrate.rb

Copy the MongoDB somewhere to somewhere else.

    mongomigrate.rb asl:drags localhost:drags

# mysqlshove

MySQL helper for creating a table directly from a csv file.

    mysqlshove somedb maps/coords.csv --table some_new_table -u root

The first column of the table should be unique integers, and it will be named `pkid`.

# nargs

One-line bash script to print out the number of arguments passed in.
Useful for debugging variables and variable expansion.

    nargs "Just two" arguments
    > 2

# now

Print out the current datetime in some variation on ISO-8601:

|output|timezone|date|time|file|eol|
|:-----|:-------|:---|:---|:---|:--|
|`2013-07-08`|UTC|True|False|False|False|
|`18:16:52`|UTC|False|True|False|False|
|`2013-07-08T18:16:52`|UTC|False|False|False|False|
|`2013-07-08T18:16:52\n`|UTC|False|False|False|True|
|`2013-07-08T18-16-52`|UTC|False|False|True|False|
|`2013-07-08`|None|True|False|False|False|
|`13:16:52`|None|False|True|False|False|
|`2013-07-08T13:16:52`|None|False|False|False|False|
|`2013-07-08T13:16:52\n`|None|False|False|False|True|
|`2013-07-08T13-16-52`|None|False|False|True|False|


```bash
$ now --utc -l
2013-07-08T18:18:51
$
```

# otf2ttf2eot.sh

Convert an OTF font file to EOT with fontforge

    otf2ttf2eot.sh TimesNewRoman.otf

# pcol

Like `col`, but auto-adjusts with more text. Slower, obviously.

    cat ANEW2010All.txt | pcol -s \\t

# pdfcat

`gs | pdftk cat output` helper.

    pdfcat page1.pdf page2.pdf bothpages.pdf

Or

    pdfcat page1.pdf page2.pdf > bothpages.pdf

# pdfcount

Just pipes `pdftotext` (comes with LaTeX, I think) through `wc -w`:

    pdfcount LSA.pdf

# pdfcropall

Given a list of PDFs, run `pdfcrop` on all of them with meager (but non-zero) margins, letting `pdfcrop` rename them as it likes.

    pdfcropall Readings/2011-10-02/*.pdf

# pdfstamp

Watermark only the first page of a PDF with another PDF.

    pdfstamp Chomsky_2012.pdf fair_use.pdf


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


# ppjson

Pretty print JSON (using Python's `json.dumps`, sorting keys and indenting by two spaces):

    cat Twitter/Texas_geolocated.json | ppjson

# ppxml

Pretty print XML using [`lxml`](http://lxml.de/) (or [`BeautifulSoup`](http://www.crummy.com/software/BeautifulSoup/), if you use the flag `-f soup`).

    ppxml APW19980322.0749.tml

Not like XML gets pretty. It just gets pretti*er*.

# prefix

Prefix file(s) with a literal string or timestamp, in the latter case, the birthtime of the specified file(s).

    prefix ExportArticle.pdf

Supposing `ExportArticle.pdf` was created on 2016-04-11, this moves `ExportArticle.pdf` to `20160411-ExportArticle.pdf`.

If the target destination exists, `prefix` exits with an error. See `prefix --help` for more options.

# prependbom

Prepend the UTF-8 byte order marker (BOM) to the input. Uses `fileinput`, so STDIN and all files supplied as command line arguments will be streamed to STDOUT after the BOM byte sequence, `\xef\xbb\xbf`.

    <flat.txt prependbom > flat.utf8

# ptx

Run `pdflatex` on the nearest `.tex` file, potentially specified by command line argument,
without interaction, and then open in `TeXShop`.

    ptx Brown_FinalReport.tex

Or

    ptx Brown_FinalReport

Or

    $ ls *.tex
    Brown_FinalReport.tex     Figures.tex     Zscores.tex

    $ ptx

I use this in Sublime Text 2 in my `LaTeX` build system.

# redis-del

Do a combo redis KEYS "prefix:*" command and then DEL whatever it finds.

    redis-del domains:*

# redismigrate

Needs to be generalized. Currently copies everything from a hard-coded remote host, "dark", (over automatically opened SSH tunnel) to localhost, using the hard-coded in "forex:*" key wildcard.

    redismigrate

But you get the idea.

# renderpage

Open up a webpage in PhantomJS and render it to an image file in the current directory. The filename is based on the given URL.

    renderpage http://irinawerning.com/bttf2/back-to-the-future-2-2011/

It outputs the filename it used, among other things.

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

# statuses

Give it the directories of your git repositories and it'll run `git status` on them all and colorize them and tell you which ones need committing and pushing.

    statuses ~/github/*/

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

# taken

Like whois-domains, take a list of domains, separated by newlines, and query whois for availability, caching in redis.

    echo henrian.com | taken

# textext

Uh, what? So it looks through lines of json and prints just the "text" attribute. I guess if you want to look as just Tweet text. Something like `npm install json` and then `cat feed.json | json -C text` would do the same thing.

# tnls

List all active ssh tunnels, looking for something like `ssh ... -L ...`.

# `trim_trailing_whitespace`

Bash script wrapper around `sed` call to delete trailing whitespace, **in-place**.

    trim_trailing_whitespace README.md

# tgz

Wrapper around `tar cz`, basically:

    tar -czf $1.tgz $1
    mv $1 $1.tmp

But with some existing / missing checks.

Use like:

    tgz penn-treebank-rel3/

# tjz

Run `tar cj` and move the original into `/tmp`:

    $ tjz table_extractor/
    created table_extractor.tar.bz2 and moved original to /tmp/table_extractor-20160117T135651

It will exit gracefully if the original does not exist, or if the target `$1.tar.bz2` file already exists.

# transpose

Super-complicated Awk script for transposing like in Excel.

    transpose alice-results.dat | pcol -g 2

# tx

Like [`ptx`](#ptx), but with a `latex && dvipdf` pipeline instead of `pdflatex`.
You'll probably only find this useful if you're still using `qtree` with arrows,
in which case you really ought to check out `TikZ`.

    tx so_many_trees

# vimeo-crawler

Crawl vimeo for the most popular movies under a given channel, saving to `~/Movies/vimeo`:

    vimeo-crawler --channels staffpicks

The destination directory is created with `os.makedirs` if it doesn't exist. See `--help` for more options.

Requires `requests`, `youtube-dl`, and `redis`:

    easy_install requests
    brew install youtube-dl
    brew install redis
    launch redis

# vsplitimg

Open all files in the current folder as images, split them into half, left and right, (like opening a normal book), and save as the original filenames suffixed with `-left` or `-right`, JPEGs with quality 95.

    cd ~/Pictures/scans
    vsplitimg *.jpg

Requires `PIL`: `brew install PIL` or `pip install -U PIL` if you're feeling optimistic

# vsplitpdf

Using `pyPdf`, open up a PDF, cropping the left and right sides right down the middle, into left and right. Create a new PDF with these crops.

    vsplitpdf reconstruction.pdf

A quick `easy_install pyPdf` may be required.

# wgetar

`wget | tar -xz` helper. Get from url and unpackage based on extension (handles `gz` and `bz2`).

    wgetar http://ftp.gnu.org/gnu/wget/wget-1.5.3.tar.gz

# whois-domains

1. Extract all strings that look something like domain names from the supplied files (uses Python's `fileinput`)
2. Fetch all the whois records using the command line `whois`
3. Cache raw whois results in Redis (using the bucket prefix `whois:`) because `whois` servers are finicky. If some whois request times out or the program crashes, simply restart the script and it will resume where it left off.
4. Extract the expiration date from the whois records and list them all, ordered from soonest expiration to most distant.

```bash
whois-domains ~/domains.yaml
```

# yaml2json

Read in YAML and output JSON.

    cat simple_spec.yaml | yaml2json | jq . > simple_spec.json

# zipf

Print out the most common words in a plain text document.

    cd ~/corpora/heliohost
    <Fre_Newspapers.txt zipf
