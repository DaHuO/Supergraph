t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = str(input().split()[0])  # read a list of integers, 2 in this case
  n = list(n)
  ans = ''
  for X in n:
  	if ans == '':
  		ans = ans + X
  	else:
  		tem1 = ans + X
  		tem2 = X + ans
  		ans = max(tem1,tem2)
  print("Case #{}: {}".format(i,ans))
  # check out .format's specification for more formatting options