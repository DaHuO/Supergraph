from random import randint
import math

def main():
  with open("C-small-attempt0.in","r") as f:
    T = f.readline()
    ll = f.readline().split(' ')
    N = int(ll[0])
    J = int(ll[1])
  print "Case #1:"
  k = 0
  l2 = []
  while k < J:
    r = randint(32768,65535)
    s = bin(r)
    r = s[2:]
    if r not in l2:
      if r.startswith("1") and r.endswith("1"):
        l = []
        r2 = int(r,2)
        l.append(is_prime(r2))
        r3 = int(r,3)
        l.append(is_prime(r3))
        r4 = int(r,4)
        l.append(is_prime(r4))
        r5 = int(r,5)
        l.append(is_prime(r5))
        r6 = int(r,6)
        l.append(is_prime(r6))
        r7 = int(r,7)
        l.append(is_prime(r7))
        r8 = int(r,8)
        l.append(is_prime(r8))
        r9 = int(r,9)
        l.append(is_prime(r9))
        r10 = int(r,10)
        l.append(is_prime(r10))
        if True not in l:
          l2.append(r)
          k = k + 1
          print r,l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return True
    
if __name__ == '__main__':
  main()
