
#!/usr/bin/python

import sys
def isDigitInStr(digit,str):
  return digit in str

def problem(number,res):
  for i in range(0,10):
    if str(i) not in res and isDigitInStr(str(i),number):
      res.append(str(i))
  return res



res = []
number = int(sys.argv[1])
number_tmp = number
if number == 0:
  print "INSOMNIA"
else:
  mul=1
  while  len(res) != 10:
    problem(str(number_tmp),res)
    mul = mul + 1
    number_tmp = number * mul

  print number_tmp - number
