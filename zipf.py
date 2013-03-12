#!/usr/bin/env python
import sys
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description='Token / type comparator.')
parser.add_argument('--char', action='store_true', help='Count by chars instead of words.')
parser.add_argument('--case', action='store_true', help='Retain case.')
parser.add_argument('--top', default=200, help='How many types to print out counts for.')
parser.add_argument('--digits', action='store_true', help='Keep digits?')
args = parser.parse_args()

import re
word_re = re.compile(r'\w+', re.U)

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

    # print tokens
    types.update(tokens)

for token, count in types.most_common(args.top):
    # if token.iswhitespace():
    # else:
    print u'%26s (%d)' % (repr(token)[2:-1], count)

