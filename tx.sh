#!/usr/bin/env sh
TEXFILES=($1)
TEXFILE=${TEXFILES[0]/\.tex/}
/usr/texbin/latex -interaction=scrollmode $TEXFILE && /usr/local/bin/dvipdf $TEXFILE && open -a TeXShop.app $TEXFILE.pdf
