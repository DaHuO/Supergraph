# C.py (Coin Jam)
# jreiter

def strToBaseN(bitString, base):
  value = 0
  i = 0
  for b in bitString[::-1]:
    value += int(b)*(base**(i))
    i += 1
  return value

def findSmallDivisor(x):
  if x%2 == 0: return 2
  for i in range(3, int(x**0.5)+1, 2):
    if x%i == 0:
      return i
    if i > 1000:
      return

def testCoin(bitString):
  divisors = []
  for i in range(2, 11):
    divisor = findSmallDivisor(strToBaseN(bitString, i))
    if divisor == None: return None
    divisors.append(divisor)
  return divisors

N = 32
J = 500
coins = 0
bits = strToBaseN("1"+"0"*(N-2)+"1", 2)

print("Case #1:")

while coins < J:
  divisors = testCoin(bin(bits)[2:])
  if divisors:
    print(bin(bits)[2:], " ".join([str(x) for x in divisors]))
    coins += 1
  bits += 1
  if bits%2 == 0:
    bits += 1