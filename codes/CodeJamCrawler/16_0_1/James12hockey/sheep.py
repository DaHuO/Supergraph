



def digs(n, x):
  while n > 0:
    t = n % 10
    n /= 10
    x[t] = 1


def counting(n):
  x = [0 for i in range(10)]
  count = 2
  curr = n
  while True:
    digs(curr,x)
    if 0 in x:
      curr = count * n
      count += 1
    else:
      break

  return curr

t = int(raw_input())
#1 2 3 ..
for tt in range(t):
  n = int(raw_input ())
  if n == 0:
    print("Case #{0}: INSOMNIA ".format(tt + 1))
  else:
    res = counting(n)
    print("Case #{0}: {1}".format(tt + 1, res))

