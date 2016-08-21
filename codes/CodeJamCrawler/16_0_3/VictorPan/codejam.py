#generate all strings from 1[0]+141 to [1]+16
#for each string, while found < J
#  check if not prime for each base from 2 to 10
#  if prime next string
#  else get divisor that works
import sys

def is_prime(n): # either True is prime or the first divisor
  if n in [2,3,5,7,11,13,17,19,23,29,31]: return True
  if n%2 == 0: return 2
  if n%3 == 0: return 3
  if n%5 == 0: return 5
  if n%7 == 0: return 7
  if n%11 == 0: return 11
  if n%13 == 0: return 13
  if n%17 == 0: return 17
  if n%19 == 0: return 19
  if n%23 == 0: return 23
  if n%29 == 0: return 29
  if n%31 == 0: return 31
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n > 1000000: return True
    if n%f == 0: return f
    if n%(f+2) == 0: return f+2
    f +=6
  return True

def solve(n,j):
  start = '1'+'0'*(n-2)+'1'
  end = '1'+'0'*n
  while (start != end) and (j > 0):
    answer = ""
    flag = True
    for b in range(2,11):
      tmp = is_prime(int(start,b))
      if tmp == True:
          flag = False
          break
      else:
        answer+=str(tmp)+" "
    if flag:
      j -= 1
      print(start+" "+answer)
    start = "{0:b}".format(int(start,2)+2)
'''
  for i in range(int(start,2),int(end,2)+1):
    if j == 0:
      break
    answer = ""
    print(answer)
'''
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, j = [int(s) for s in input().split(" ")]
  print("Case #{}:".format(i))
  solve(n,j)
