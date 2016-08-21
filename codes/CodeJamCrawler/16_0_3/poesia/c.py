import string
import random
digs = string.digits + string.ascii_letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x = x // base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def random_pal(n):
    s = "1"
    while len(s) < n // 2:
        s += '01'[random.randint(0,1)]
    return s + ''.join(reversed(s))

def get_fac(n):
    for i in range(2, n):
        if n % i == 0:
            return i

N, J = 32, 500

print("Case #1:")
gone = set()

while len(gone) < J:
    x = random_pal(N)
    if x in gone:
        continue
    gone.add(x)
    divs = []
    for b in range(2, 11):
        divs.append(get_fac(int(x, b)))
    print("{} {}".format(x, " ".join(map(str, divs))))
