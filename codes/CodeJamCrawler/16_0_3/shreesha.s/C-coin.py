import math

def prime(p):
  limit = int(math.ceil(math.sqrt(p)))
  for z in range(2, limit):
    if p%z == 0:
      return z
  return -1

t = int(raw_input())
for i in range(t):
  n, j = map(int, raw_input().split())
  count = 0
  print "Case #1:"
  for w in range(pow(2, n-2)):
    ans = "1"+bin(w)[2:].zfill(n-2)+"1"
    ans = ans.replace(" ", "")
    for k in range(2, 11):
      bin_num = "1"+bin(w)[2:].zfill(n-2)+"1"
      bin_num = bin_num.replace(" ", "")
      num = int(bin_num, k)
      flag = prime(num)
      if flag == -1:
        break
      else:
        ans += " " + str(flag)
    if flag != -1:
      print ans
      count += 1
      if count == j:
        break
    else:
      continue

 
