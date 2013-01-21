#!/usr/bin/env python
from collections import Counter
import re
import fileinput

word_re = re.compile(r'\w+', re.U)

counts = Counter()
for line in fileinput.input():
    tokens = word_re.findall(line.decode('utf8').lower())
    words = [token for token in tokens if not token.isdigit()]
    counts.update(tokens)

for token, count in counts.most_common(200):
    print u'%26s (%d)' % (token, count)
