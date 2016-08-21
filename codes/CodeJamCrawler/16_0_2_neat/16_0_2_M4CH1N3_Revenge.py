def pancake_flip(s):
  if s.find('-') == -1:
    return 0
  if len(s) <= 1:
    return 1
  
  # assert: at least 1 '-' exists
  s = [True if x=='+' else False for x in s]
  flips = 0

  while True:
    
    for x in range(len(s)-1, -1, -1):
      if s[x] == False:
        index = x
        break

    s = [not x for x in s[:index+1]] + s[index+1:]
    flips += 1
  
    if all(s): break

  return flips
    

T = int(input().strip())
filehandle = open('output.txt','w')
for i in range(T):
  ans = pancake_flip(input().strip())
  print('Case #{}: {}'.format(i+1, ans),file=filehandle) 
