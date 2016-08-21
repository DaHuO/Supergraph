def sleep(s):
  for i in range(10):
    if(not (str(i) in s)):
      return False
  return True

def solve(x):
  if(x == 0):
    return 'INSOMNIA'
  seen = set([])
  i = 0
  while(not sleep(seen)):
    i += 1
    for char in str(x*i):
      seen.add(char)
  return x*i

T = int(raw_input().strip())
for t in range(1,T+1):
  print "Case #" + str(t) + ":",
  N = int(raw_input().strip())
  print solve(N)
