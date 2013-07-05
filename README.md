# scripts

Some handy short scripts I like, many of which I've written all by myself!

## Installation

```bash
cd ~
git clone git://github.com/chbrown/scripts.git
echo 'export PATH=$HOME/scripts:$PATH >> .bashrc.local
```

Prerequisite for many of these scripts:

```bash
pip install requests colorama
```

## License

Copyright © 2012–2013 Christopher Brown. [MIT Licensed](LICENSE).

Except for following files, I am the sole author of all of these scripts.

* autoreload
* htpasswd.py
* otf2ttf2eot.sh
* soundcloud
* transpose

---

# alphadec

Create 10 alphadecimal passwords of length 16 each.

    alphadec --length 16 --count 10


# autoreload

Watch a directory for changed files and restart a process when a change is detected.

    autoreload python main.py

From [stevekrenzel/autoreload](https://github.com/stevekrenzel/autoreload) (no license).

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

# fit

One-liner for when you have some lengthy lines and you want to kill the wrap:

    tr '\t' ' ' | cut -c -$(tput cols)

# git-remote-tags

Wrapping around `git ls-remote --tags git://...` to get the good stuff:

    git-remote-tags chbrown/amulet

Assumes github.

# git-submodule-rm

Until git 1.8.3 rolls around:

    git-submodule-rm static/lib

Thanks goes to [stackoverflow](http://stackoverflow.com/questions/1260748/how-do-i-remove-a-git-submodule).

# htpasswd.py

Script originally from a guy named "Eli Carter."

After `alphadec`'ing a password, say, `vsw8lq4NuM0S`, create an `htpasswd` file called `nginx.htpasswd` with that password for the user `scriptuser`. I think it adds to an existing file if `nginx.htpasswd` already exists.

    htpasswd.py -c -b nginx.htpasswd scriptuser vsw8lq4NuM0S

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

MD5 hash the last command line argument.

    md5py freshplum

# mongomigrate.rb

Copy the MongoDB somewhere to somewhere else.

    mongomigrate.rb asl:drags localhost:drags

# mysqlshove

MySQL helper for creating a table directly from a csv file.

    mysqlshove somedb maps/coords.csv --table some_new_table -u root

The first column of the table should be unique integers, and it will be named `pkid`.

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

# pg_migrate

Like mongomigrate, but shorter (and not ruby)!

    pg_migrate dark:twitter_dev localhost:twitter_dev

Uses `ssh -C` and `pg_dump` but that's about it. You'll need to `dropdb` and `createdb`, etc., yourself.

# pip-update-all

Simply do a `pip install -U <package>` on all your installed packages.

    pip-update-all

# ppjson

Pretty print JSON (using Python's `json.dumps`, sorting keys and indenting by two spaces):

    cat Twitter/Texas_geolocated.json | ppjson

# ppxml

Pretty print xml, using Python's `BeautifulSoup`.

    ppxml timeml/APW19980322.0749.tml

Not like xml gets pretty. It just gets pretti*er*.

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

# sf

Little helper for the awesome `sshfs` tool that OS X Fuse provides. It'll make the given directory as needed, and die quietly if the connection already exists.

    sf tacc: /Volumes/tacc

# soundcloud

Python rendition of Luka Pusic's soundcloud.sh downloader. His wasn't unescaping higher order Unicode character escapes. Well, the Mac OS X filesystem totally supports UTF-8, and this script does too.

    soundcloud https://soundcloud.com/oskmusic

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

# textext

Uh, what? So it looks through lines of json and prints just the "text" attribute. I guess if you want to look as just Tweet text. Something like `npm install json` and then `cat feed.json | json -C text` would do the same thing.

# tnls

List all active ssh tunnels, looking for something like `ssh ... -L ...`.

# tgz

Wrapper around `tar cz`, basically:

    tar -czf $1.tgz $1
    mv $1 $1.tmp

But with some existing / missing checks.

Use like:

    tgz penn-treebank-rel3/

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

    pip install requests
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

A quick `pip install pyPdf` may be required.

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

Using Python's yaml and json modules, read in yaml and output json. Useful because Node.js's YAML support used to suck.

    cat simple_spec.yaml | yaml2json > simple_spec.json

# zipf

Print out the most common words in a plain text document.

    cd ~/corpora/heliohost
    <Fre_Newspapers.txt zipf
