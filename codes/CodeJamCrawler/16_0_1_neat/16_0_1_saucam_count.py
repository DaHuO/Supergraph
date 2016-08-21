import sys

t = int(sys.stdin.readline())

for i in range(0, t):
  n = int(sys.stdin.readline())
  arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  
  
  gSet = set()
  m = 0
  if n == 0:
    print("Case #%d: %s"% ((i+1), "INSOMNIA"))
  else:  
    while len(gSet) != 10:
      m = m + n
      nString = str(m)
      gSet.update(set(nString))

    '''for ch in nString:
        if (arr[ch-'0'] == 0):
          arr[ch-'0'] = 1
          cntr++;
    '''

    print("Case #%d: %d"% ((i+1), m))

