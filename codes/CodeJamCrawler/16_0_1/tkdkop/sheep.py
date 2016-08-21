#!/usr/bin/env python
import sys


m = sys.stdin.readline()
i = 0
for line in sys.stdin.readlines():
    n = int(line)
    i += 1
    out_str = "Case #%d: " % i

    if n == 0:
        out_str += 'INSOMNIA'
        print out_str
        continue
    last_number = n
    counter = 1
    seen_chars = set()
    while len(seen_chars) < 10:
        last_number = counter*n
        [seen_chars.add(c) for c in str(last_number)]
        counter += 1
    out_str += str(last_number)

    print out_str
