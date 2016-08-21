num = []

def tobase (n, b):
  result = 0
  power = 1
  for i in range(len(n)):
    result += power * n[len(n) - 1 - i]
    power *= b
  return result
  
def is_prime(n):
  for i in range(2, 10000):
    if n % i == 0:
      return i
  return 0

def add_one(num):
  k = len(num) - 2
  while k > 1:
    if num[k] == 0:
      num[k] = 1
      break;
    else:
      num[k] = 0
      k -= 1
  return 0

T = 1##int(input())
for t in range(T):
  print "Case #" + str(t+1) + ":"
  ##a = input().split()
  N = 32##int(a[0])
  J = 500#int(a[1])
  num.append(1)
  for i in range(N-2):
    num.append(0)
  num.append(1)
  printed = 0
  while printed < J:
    proof = [0] * 9
    prime = False
    for i in range (9):
      n = tobase(num, i+2)
      proof[i] = is_prime(n)
      if proof[i] == 0:
	prime = True
    if not prime:
      coin = ''.join(str(x) for x in num)
      print coin,
      for i in range(8):
	print proof[i],
      print proof[8]
      printed += 1
    done = add_one(num)
  
  #print(printed)
  #print(tobase(num, 10))
  
  
  

