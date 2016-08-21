def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())
def digits(N):
  digits = set()
  while N:
    digits.add(N%10)
    N = N/10
  return digits

_T = readint()
for _t in range(_T):
  found = set()
  oldlen = 0
  N = readint()
  res = N
  counter = 0

  while True:
    found.update(digits(res))
    if len(found) == 10:
      break
    if len(found) == oldlen:
      counter = counter + 1
      if counter >= 100:
        break
    oldlen = len(found)
    res = res + N
    
  if len(found) == 10:
    print "Case #%i: " %(_t+1), res
  else:
    print "Case #%i: INSOMNIA" %(_t+1)
