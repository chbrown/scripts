# Some scripts I like, most of which I've written all by myself!

Except for `htpasswd.py`, `soundcloud`, and `transpose` all of these scripts were written by me and are Copyright 2012-2013 Christopher Brown, released here under the MIT License.

## Prereqs:

    pip install requests

# alphadec

Create 10 alphadecimal passwords of length 16 each.

    alphadec --length 16 --count 10

# click

Measured from the top left of the screen, left-click once.

    click -x 600 -y 400

# csv2html

E.g.,

    csv2html batch_results.csv > batch_results.csv.html

# csv2tsv

Uses Python's dialects to convert.

    cat sb5b.csv | tr '\r' '\n' | csv2tsv > sb5b.tsv

# fit

One-liner for when you have some lengthy lines and you want to kill the wrap:

    tr '\t' ' ' | cut -c -$(tput cols)

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

# otf2ttf2eot.sh

Convert an OTF font file to EOT with fontforge

    otf2ttf2eot.sh TimesNewRoman.otf

# pcol

Like `col`, but auto-adjusts with more text. Slower, obviously.

    cat ANEW2010All.txt | pcol -s \\t

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

# ptx.sh

Run `pdflatex` on the nearest `.tex` file, without interaction, and then open in `TeXShop`.

    ptx Brown_FinalReport.pdf

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

# stopwatch

Basic duration timer.

    stopwatch
    > Press \n to end.
    ↪
    > 1.3509s

# textext

Uh, what? So it looks through lines of json and prints just the "text" attribute. I guess if you want to look as just Tweet text. Something like `npm install json` and then `cat feed.json | json -C text` would do the same thing.

# transpose

Super-complicated Awk script for transposing like in Excel.

    transpose alice-results.dat | pcol -g 2

# tx.sh

Like `ptx.sh`, but with a `latex` && `dvipdf` pipeline instead of `pdflatex`. In case you're still using `qtree` with arrows. (In which case you really ought to check out TikZ.)

    tx.sh so_many_trees

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

# whois-domain-yaml

Using a Yaml file formatted something like this:

    ---
    sites:
      - henrian.com
      - mehenry.com
    personal:
      - cal0.com

etc., get all the whois records using the command line `whois`, cache them in Redis in case it times out, and return them all, ordered from next expiration to most distant expiration.

    whois-domain-yaml that.yaml

# yaml2json

Using Python's yaml and json modules, read in yaml and output json. Useful because Node.js's YAML support used to suck.

    cat simple_spec.yaml | yaml2json > simple_spec.json

# zipf.py

Print out the most common words in a plain text document.

    cd ~/corpora/heliohost
    zipf.py Fre_Newspapers.txt
