import sys

def CheckPrimeReturnDivisor(number):
  result = 0;
  #NOTE(ken): input will always be > 2
  if(number % 2 != 0):
    i = 3
    while(i*i < number and i < 1024):
        if(number % i == 0 ):
          result = i
          break
        i += 2
  else:
    result = 2
  return result

def IncrementJamcoinStr(jamcoin):
  for i in range(len(jamcoin)-2, 0, -1):
      if jamcoin[i] == '1':
          jamcoin = jamcoin[:i] + '0' + jamcoin[i+1:]
      else:
          jamcoin = jamcoin[:i] + '1' + jamcoin[i+1:]
          break
  return jamcoin

inputStrings = open('C-large.in', 'r').read().splitlines()
# inputStrings = open('C-small-attempt0.in', 'r').read().splitlines()

caseNum = int(inputStrings[0])
inNums = inputStrings[1].split()
jamcoinLength = int(inNums[0])
jamcoinNum = int(inNums[1])

currentJamcoin = "1";
for i in range(0,jamcoinLength-2):
    currentJamcoin += "0"
currentJamcoin += "1"

outString = "Case #1:\n"

currentJamcoinNum = 0
while(currentJamcoinNum < jamcoinNum):
    found = True
    divisors = [0] * 9

    for i in range(2, 11):
        value = int(currentJamcoin,i)
        divisor = CheckPrimeReturnDivisor(value)
        if divisor != 0:
            divisors[i-2] = divisor
        else:
            found = False
            break

    if found:
        outString += str(currentJamcoin)
        for i in range(0,9):
            outString += " " + str(divisors[i])
        outString += "\n"

        currentJamcoin = IncrementJamcoinStr(currentJamcoin)
        currentJamcoinNum += 1
        # print(str(currentJamcoinNum))
    else:
        currentJamcoin = IncrementJamcoinStr(currentJamcoin)



fileOut = open('C-large.out', 'w')
# fileOut = open('C-small-attempt0.out', 'w')
fileOut.write(outString)
fileOut.close()
