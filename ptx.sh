#!/usr/bin/env sh
TEXFILES=($1)
TEXFILE=${TEXFILES[0]/\.tex/}
/usr/texbin/pdflatex -interaction=scrollmode $TEXFILE && open -a TeXShop.app $TEXFILE.pdf
