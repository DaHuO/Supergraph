T = int(raw_input())

def is_valid(str):
  for char in str:
    if char == '-': return False
  return True

def process(str):
  if is_valid(str): return 0
  n = 0
  if str[0] == '-': 
    n+=1
    flag = False
    for i in range(1, len(str)):
      if str[i] == '+':
        flag = True
      if str[i] == '-' and flag:
        flag = False
        n+=2
  elif str[0] == '+':
    flag = True
    for i in range(1, len(str)):
      if str[i] == '-' and flag:
        flag = False
        n += 2
      if str[i] == '+':
        flag = True
  return n

for i in range(1, T+1):
  N = raw_input()
  print('Case #{}: {}'.format(i, process(N)))

