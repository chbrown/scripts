#!/usr/bin/env python
import sys
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description='Token / type comparator.')
parser.add_argument('--char', action='store_true', help='Count by chars instead of words.')
parser.add_argument('--case', action='store_true', help='Retain case.')
parser.add_argument('--top', default=200, type=int, help='How many types to print out counts for. (default: 200)')
parser.add_argument('--digits', action='store_true', help='Keep digits?')
args = parser.parse_args()

import re
word_re = re.compile(r'\w+', re.U)

wc = 0
types = Counter()
for raw in sys.stdin:
    line = raw.decode('utf8')
    if not args.case:
        line = line.lower()

    if args.char:
        tokens = list(line)
    else:
        tokens = word_re.findall(line)

    if not args.digits:
        tokens = filter(lambda x: not x.isdigit(), tokens)

    wc += len(tokens)
    types.update(tokens)

print u'%26s %7s %9s' % ('token', 'count', 'freq')
for token, count in types.most_common(args.top):
    # if token.iswhitespace():
    # else:
    print u'%26s %7d %8.4f%%' % (repr(token)[2:-1], count, count * 100.0 / wc)
