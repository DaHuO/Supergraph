from copy import deepcopy

def init(st):
  S['E'] = 0;
  S['R'] = 0;
  S['O'] = 0;
  S['N'] = 0;
  S['T'] = 0;
  S['I'] = 0;
  S['H'] = 0;
  S['V'] = 0;
  S['F'] = 0;
  S['S'] = 0;
  S['Z'] = 0;
  S['W'] = 0;
  S['U'] = 0;
  S['X'] = 0;
  S['G'] = 0;
  for s in st:
    S[s] += 1

def has(word):
  for c in word:
    S[c] -= 1

def solve():
  if(S['Z'] > 0):
    has('ZERO')
    nums.append(0)
    return solve()
  elif(S['W'] > 0):
    has('TWO')
    nums.append(2)
    return solve()
  elif(S['U'] > 0):
    has('FOUR')
    nums.append(4)
    return solve()
  elif(S['X'] > 0):
    has('SIX')
    nums.append(6)
    return solve()
  elif(S['G'] > 0):
    has('EIGHT')
    nums.append(8)
    return solve()
############################################################
  elif(S['H'] > 0):
    has('THREE')
    nums.append(3)
    return solve()
  elif(S['F'] > 0):
    has('FIVE')
    nums.append(5)
    return solve()
  elif(S['S'] > 0):
    has('SEVEN')
    nums.append(7)
    return solve()
  elif(S['O'] > 0):
    has('ONE')
    nums.append(1)
    return solve()
  elif(S['N'] > 0):
    has('NINE')
    nums.append(9)
    return solve()
  else:
    ans = ''
    nums.sort()
    for i in nums:
      ans += str(i)
    return ans

T = int(raw_input().strip())

for x in range(1,T+1):
  print 'Case #' + str(x) + ':',
  st = raw_input().strip()
  S = {}
  nums = []
  init(st)
  print solve()
