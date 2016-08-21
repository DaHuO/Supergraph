t= int(raw_input())
for i in range(t):
  inp = raw_input()
  leng = len(inp)
  flag = 0
  if inp[leng-1] == '-':
    ans = 1
    flag = 1
  else:
    ans = 0
  for j in range(leng-2, -1, -1):
    if inp[j] == '+' and flag == 1:
      ans += 1
      flag = 0
    elif inp[j] == '-' and flag == 0:
      ans += 1
      flag = 1
  print "Case #%d:" %(i+1),
  print ans
