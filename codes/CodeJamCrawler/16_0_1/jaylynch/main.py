#!/usr/local/bin/python
DEBUG = False

def count_sheep(n):
    if n == 0:
        return "INSOMNIA"

    cn = n
    seen_digits = [
        False, False, False, False, False,
        False, False, False, False, False
    ]

    for c in str(cn):
        if DEBUG:
            print seen_digits
        seen_digits[int(c)] = True

    while sum(seen_digits) < 10:
        cn += n
        for c in str(cn):
            seen_digits[int(c)] = True
    
    return cn

t = int(raw_input())
for i in xrange(1, t + 1):
  n = int(raw_input())
  print "Case #{}: {}".format(i, count_sheep(n))
