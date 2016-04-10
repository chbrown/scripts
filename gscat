#!/usr/bin/env bash

if [[ "${@---help}" =~ '--help' ]]; then
  printf "The first argument should be the PDF filename\n"
  printf "Writes to a .gs.pdf file in the current directory\n\n"
  printf "  Example: gscat sciencey_article.pdf\n"
  exit 1
fi

INPUT_FILENAME=$1
OUTPUT_FILENAME="${INPUT_FILENAME%.pdf}.gs.pdf"

# set -x
printf "Ghostscript writing '%s' to '%s'" "$INPUT_FILENAME" "$OUTPUT_FILENAME\n"

# gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=${temp_pdf_path} opts.input
# The -o option also sets the -dBATCH and -dNOPAUSE options.
gs -q -sDEVICE=pdfwrite -o "$OUTPUT_FILENAME" "$INPUT_FILENAME"
