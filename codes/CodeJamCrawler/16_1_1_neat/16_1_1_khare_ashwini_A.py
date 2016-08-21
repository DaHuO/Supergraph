from collections import deque
T = int(raw_input())

def process(s):
  arrangement = deque(s[0])
  for i in range(1, len(s)):
    if s[i] >= arrangement[0]:
      arrangement.appendleft(s[i])
    else:
      arrangement.append(s[i])
  lastword = []
  for el in arrangement:
    lastword.append(el)
  return ''.join(lastword)

for case in range(1, T+1):
  S = raw_input()
  print('Case #{}: {}'.format(case, process(S)))