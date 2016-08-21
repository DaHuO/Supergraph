#!/usr/local/bin/python
DEBUG = False

import math

def first_factor(n):
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i

    return False

def test_str(n):
    if DEBUG:
        print n
    assert(sorted(set('01' + n)) == ['0', '1'])
    ffs = []
    for b in xrange(2, 11):
        b_n = int(n, b)
        ff = first_factor(b_n)
        if not ff:
            return False
        if DEBUG:
            print '%s: %s (%s)' % (b, b_n, ff)
        ffs.append(ff)

    return ffs

def bstr(i):
    return bin(i)[2:]

def test_int(n):
    return test_str(bstr(n))

def get_candidates(n):
    value = int('1' + '1'.zfill(n-1), 2)
    while len(bstr(value)) == n:
        yield value
        value += 0b10

t = int(raw_input())
for i in xrange(1, t + 1):
  n, j = [int(s) for s in raw_input().split(" ")]
  results = []

  candidates = get_candidates(n)
  for candidate in candidates:
    result = test_int(candidate)
    if result:
        results.append("{} {}".format(bstr(candidate), ' '.join(str(r) for r in result)))
    if len(results) == j:
        break

  print "Case #{}:".format(i)
  for result in results:
    print result
