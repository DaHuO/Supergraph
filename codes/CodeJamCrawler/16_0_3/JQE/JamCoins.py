import math

def convertbasetoten(num, base):
    baseten = 0
    power = 0
    for c in reversed(num):
        baseten += int(c)*math.pow(base,power)
        power += 1
    return int(baseten)

#Returns divisor or -1 if prime, from stackoverflow.com answer
def is_prime(n):
  if n == 2 or n == 3: return -1
  if n < 2 or n%2 == 0: return 2
  if n < 9: return -1
  if n%3 == 0: return 3
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return f
    if n%(f+2) == 0: return (f+2)
    f +=6
  return -1

input = open("C-small-attempt1.in", "r")
cases = int(input.readline())
jamcoins = {}

for case in range(cases):
    print("Case #{}:".format(case+1))
    NJ = input.readline().split()
    N = int(NJ[0])
    J = int(NJ[1])
    x = 0
    success = 0
    while success < J:
        maybejamcoin = "1" + bin(x)[2:].zfill(N-2) + "1"
        divisors = []
        for base in range(2,11):
            test = convertbasetoten(maybejamcoin, base)
            ok = is_prime(test)
            if ok == -1:
                break
            divisors.append(ok)
        if len(divisors) == 9:
            success += 1
            print("{0} {1}".format(maybejamcoin, " ".join(map(str,divisors))))
        x += 1
        
    