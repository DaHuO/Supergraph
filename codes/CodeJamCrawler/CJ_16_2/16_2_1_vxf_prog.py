from pprint import pprint
import itertools

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

ncount = []
nfreq = []

for n in numbers :
  f = {}
  for c in list(set(n)) :
    f[c] = n.count(c)
    
  nfreq.append(f)
  ncount.append(len(n))

# pprint(nfreq)

def genNumber():
  for i in range(1, 2001):
    for n in map(''.join, itertools.combinations_with_replacement('0123456789', i)):
    # itertools.product('0123456789', repeat=i)):
      l = 0
      f = {}
      for c in n :
        o = ord(c) - 48
        y = nfreq[o]
        for key, value in y.iteritems():
          if key in f :
            f[key] = f[key] + value
          else :
            f[key] = value
        l = l + ncount[o]
      #if n == '0001' :
      #  pprint((l, f))
      yield (l, f, n)

def solveCase(S):
  x = 0
  
  p = []
  
  l = len(S)
  f = {}
  for c in list(set(S)) :
    f[c] = S.count(c)
    
  # print((l,f))
    
  for gl, gf, gn in genNumber():
    # pprint((gl, gf, gn))
    if gl != l :
      continue

    good = True
    for gc, gf in gf.iteritems() :
      if not gc in f or f[gc] != gf :
        good = False

    if good :
      return gn
        
  
    
  return x

with open("A-small-attempt1.in") as f :
  t = f.readline()
  t = int(t)
  for i in range(t) :
    S = f.readline().strip()
    y = solveCase(S)

    print("Case #%d: %s" % (i + 1, y))
