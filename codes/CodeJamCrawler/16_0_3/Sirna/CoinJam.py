
import sys
import math

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


def get_first_divisor(div):
    n = 2
    while n < div:
        if div % n == 0:
            return str(n)
        n += 1


def all_ans(number):
    sys.stdout.write(number + " ")
    for _ in range(2, 11):
        x = int(number, _)
        sys.stdout.write(get_first_divisor(x))
        sys.stdout.write(" ")
    sys.stdout.write("\n")


def is_coin_jam(string):
    if string[0] != '1' or string[15] != '1':
        return False
    for _ in range(2, 11):
        x = int(string, _)
        if is_prime(x):
            return False
    return True

start = 32850
ans = 0
print "Case #1:"
while ans < 50:
    tmp = bin(start)[2:]
    if is_coin_jam(tmp):
        ans += 1
        all_ans(tmp)
    start += 1

