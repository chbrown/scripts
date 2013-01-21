#!/bin/sh
# Convert an OTF font int TTF an EOT formats.
otfFont="$1.otf"
ttfFont="$1.ttf"
woffFont="$1.woff"
fontforge -c '
    Open("'$otfFont'");
    Generate("'$ttfFont'");
    Generate("'$woffFont'");
    Quit(0);'
eotFont="$1.eot"
ttf2eot $ttfFont > $eotFont

