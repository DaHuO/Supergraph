#!/grid/common/pkgs/python/v3.2.2/bin/python3
import os,sys,glob,random;

def notprime(x, prime):
  for i in range(len(prime)):
    if x<=int(prime[i]):
      return 0
    if x%int(prime[i])==0:
      return int(prime[i])
  return 0

def getarr(N):
  arr = [1]
  for i in range(N-2):
    arr.append(random.randint(0,1))
  arr.append(1)
  return arr

def getint(arr, base):
  res = 0
  m = 1
  for i in range(len(arr)):
    res = res + arr[i]*m;
    m = m * base
  return res

def sol(arr, prime):
  for i in range(2,11):
    num = getint(arr, i)
    divisor = notprime(num, prime)
    if divisor==0:
      return

  print (getint(arr,10),end='')
  for i in range(2,11):
    num = getint(arr, i)
    divisor = notprime(num, prime)
    print (' ',end='')
    print (divisor,end='')
  print ('\n',end='')

if __name__ == '__main__':
  plist = open('x.txt', 'r')
  prime = plist.readline().split(',')

  print ('Case #1:')
  N = 16
  J = 50

  for i in range(1000):
    arr = getarr(N)
    sol(arr, prime)

