from gmpy2 import mpz
from gmpy2 import digits

n = 32
j = 500
t = 2 ** (n - 1) + 1;

res = 0
while res < j:
  x = mpz(t)
  s = x.digits(2)
  ans = [];
  for base in range (2, 11):
    cur = int(s,base)
    for div in range (2, 1000):
      if cur % div == 0:
        ans.append(div)
        break;
  if len(ans) == 9:
    print (s + " " + " ".join(map(str, ans)))
    res += 1
  t += 2

