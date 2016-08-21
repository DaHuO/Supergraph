import numpy as np


def primes(n):
  """ Input n>=6, Returns a array of primes, 2 <= p < n """
  sieve = np.ones(n/3 + (n % 6 == 2), dtype=np.bool)
  sieve[0] = False
  for i in xrange(int(n**0.5)/3+1):
    if sieve[i]:
      k = 3 * i + 1 | 1
      sieve[((k*k)/3)::2*k] = False
      sieve[(k*k+4*k-2*k*(i & 1))/3::2*k] = False
  return np.r_[2, 3, ((3*np.nonzero(sieve)[0]+1) | 1)]

t = int(raw_input())
n, j = map(int, raw_input().split())

centerdigit = 0
cnt = 0
outstr = "Case #1:"

prime_list = primes(int(int("1"*(n-15), 10)**0.5))

while True:
  digitstr = "1" + bin(centerdigit)[2:].zfill(n-2) + "1"
  if len(digitstr) > n:
    break
  divisor = []
  for i in range(2, 11):
    num = int(digitstr, i)

    if num < 4:
      break

    tmp = 0
    flag = False
    len_pl = len(prime_list)
    while True:
      if tmp == len_pl:
        break
      if prime_list[tmp] >= num:
        break
      if num % prime_list[tmp] == 0:
        flag = True
        break
      else:
        tmp += 1

    if flag:
      divisor.append(prime_list[tmp])
    else:
      break

  if len(divisor) == 9:
    outstr += "\n" + digitstr + " " + " ".join(map(str, divisor))
    cnt += 1
  if cnt == j:
    break
  centerdigit += 1

print(outstr)
