import sys
import math
import itertools as it
import operator as op
import fractions as fr


def f(s):
  d = dict()
  for c in s:
    d.setdefault(c, 0)
    d[c] += 1
  return d

digits = ["ZERO", "TWO", "FOUR", "SIX", "EIGHT", "THREE", "SEVEN", "FIVE", "NINE", "ONE"]
digits_nb = [0,2,4,6,8,3,7,5,9,1]
digits = map(lambda s: f(s), digits)

t = int(sys.stdin.readline())
for tc in range(1,t+1):
  s = sys.stdin.readline().strip()

  ds = f(s)
  
  r = []
  for i in range(10):
    digit = digits[i]
    while True:
      t = filter(lambda (ch,cnt): ch in ds and ds[ch] >= cnt, digit.iteritems())
      if len(t) == len(digit):
        r.append(digits_nb[i])
        for ch,cnt in t:
          ds[ch] -= cnt
      else:
        break

  assert(sum(ds.values()) == 0)
  print('Case #{}: {}'.format(tc, "".join(map(str,sorted(r)))))
