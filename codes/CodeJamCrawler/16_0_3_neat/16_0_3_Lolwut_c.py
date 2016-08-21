import math
N = 16
J = 50

def isPrime(num):
  for i in range(2, int(math.sqrt(num) + 1)):
    if num % i == 0:
      return i
  return 0 # prime


j = 0

print "Case #1:"
currNum = 0
while j < J:
  currNumString = "1" + bin(currNum)[2:].zfill(N-2) + "1"
  nums = [0]*9
  valid = True
  for i in range(2, 11):
    temp = isPrime(int(currNumString, i))
    if temp == 0:
      valid = False
      break
    else:
      nums[i-2] = temp
  if valid:
    j += 1
    toPrint = currNumString
    for num in nums:
      toPrint += " " + str(num)
    print toPrint
  currNum += 1

