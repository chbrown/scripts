#!/usr/bin/env bash

set -e # exit on first command that fails

usage() {
  >&2 cat <<HELP
Usage: $(basename "$0") URL [CODE] [URL [CODE] [...]]

Use the git.io URL shortener (https://git.io/blog-announcement) to shorten GitHub.com URLs.

Any CODE arguments will be paired up with URL arguments (which must start with "http") in order.
They are optional, and any unpaired URLs will be shortened with the default code.

Options:
  -h, --help     Show this usage message.
  -v, --verbose  Print extra information.
HELP
}

URLS=()
CODES=()
while [[ $# -gt 0 ]]; do
  case $1 in
    -v|--verbose)
      >&2 printf 'Entering debug (verbose) mode.\n'
      set -x
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    http*)
      URLS+=("$1")
      ;;
    *)
      CODES+=("$1")
      ;;
  esac
  shift
done

shorten() {
  # Usage: shorten URL [CODE]
  CURL_ARGS=(--form "url=$1")
  >&2 printf 'Shortening "%s"' "$1"
  if [[ -n "$2" ]]; then
    # $2 is not null => add the "code" field
    CURL_ARGS+=(--form "code=$2")
    >&2 printf ' with code "%s"' "$2"
  fi
  >&2 printf '\n'
  # --include causes the response HTTP headers to be included in the output
  # (the body of the response from git.io is the original URL)
  curl --silent --include "${CURL_ARGS[@]}" https://git.io \
  | sed -n 's/^Location: //p'
}

for index in "${!URLS[@]}"; do
  URL=${URLS[$index]}
  CODE=${CODES[$index]}
  shorten "$URL" "$CODE"
done
