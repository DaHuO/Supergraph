#!/usr/bin/python

import sys

def is_prime(n):
  if n == 2 or n == 3: return 1
  if n < 2 or n%2 == 0: return 2
  if n < 9: return 1
  if n%3 == 0: return 3
  r = 50
  f = 5
  while f <= r:
    if n%f == 0: return f
    if n%(f+2) == 0: return f+2
    f +=6
  return 1

def generateCoin(last):
  return str(bin(int(last,2) + int("10",2)))[2:]

print "Case #1:"

def printDiv(number):
  res=[]
  result = number
  for i in range(2,11):
    num = int(number,i)
    divide =  str(is_prime(num))
    if str(divide) != "1":
      res.append(divide)
    else:
      return "-1"
  if len(res) == 9:
    for j in res:
      result = result + " " + j
  return result

coin = "10000000000000000000000000000001"
find = 0
while len(str(coin)) == 32 and str(coin)[0] == "1" and find < 500:
  listDiv =printDiv(coin)
  if listDiv != "-1":
    find = find + 1
    print listDiv
  coin = generateCoin(coin)
