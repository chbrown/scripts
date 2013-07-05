#!/usr/bin/env bash
RTEXFILES=($1)
RTEXFILE=${RTEXFILES[0]/\.Rtex/}
echo Knitting $RTEXFILE
Rscript -e "library(knitr); knit(\"$RTEXFILE.Rtex\")" && pdflatex -interaction=scrollmode $RTEXFILE && open -a TeXShop.app $RTEXFILE.pdf
