def f(s):
  #print(s)
  if len(s)==0:
    return 0
  res = 0
  cnt = 0
  l = len(s)-1
  for i in range(len(s)):
    if s[l-i] == '+':
      cnt += 1
    else:
      break
  if cnt > 0:
    s = s[:-cnt]
  #print(s)
  cnt = 0
  for i in range(len(s)):
    if s[i] == '-':
      cnt += 1
    else:
      break
  if cnt > 0:
    res += 1
    s = s[cnt:]
    s = s[::-1]
    for i in range(len(s)):
      if s[i] == '+':
        s[i] = '-'
      else:
        s[i] = '+'
  #print(s)
  cnt = 0
  for i in range(len(s)):
    if s[i] == '+':
      s[i] = '-'
      cnt += 1
    else:
      break
  if cnt > 0:
    res += 1
  res += f(s)
  return res

for tc in range(int(input())):
  print('Case #{_tc}: {_sol}'.format(_tc=tc+1, _sol=f(list(input()))))

