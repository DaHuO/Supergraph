import math
N = 16
J = 50
done = 0
fo = open('CJ.out', 'w')
def isComp(x):
    for i in range(2, math.ceil(math.sqrt(x))+1 ):
        if x % i == 0:
            return i
    return -1
def convBase(s, base):
  n = 0
  for i in range(len(s)):
    if s[i]=="1":
      n += base**(len(s)-i-1)
  return n
def genCoin(i) :
  b = str(bin(i))[2:]
  n = "0" * (N-2-len(b)) + b
  return "1"+ n +"1"

raw = 0
fo.write("Case #1:\n")
while (done < J):
  prime = False
  divisors = []
  coin = genCoin(raw)
  for i in range(2, 11):
    num = convBase(coin, i)

    if (isComp(num) == -1):
      prime = True
      break
    else:
      divisors.append(isComp(num))
  raw += 1
  if(not prime):
    done+= 1
    fo.write(coin+" ")
    for i in divisors:
      fo.write("%d "%i)
    fo.write("\n")

fo.close()
