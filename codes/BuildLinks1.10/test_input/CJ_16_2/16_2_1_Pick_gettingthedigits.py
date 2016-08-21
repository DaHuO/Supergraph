import string
num = [0 for i in range(10)]
num[0] ={ 'E':1,'Z':1,'R':1,'O':1}
num[1] ={ 'O':1,'N':1,'E':1 }
num[2] ={ 'T':1,'W':1,'O':1 }
num[3] ={ 'T':1,'H':1,'R':1,'E':2}
num[4] ={ 'F':1,'O':1,'U':1,'R':1 }
num[5] ={ 'F':1,'I':1,'V':1,'E':1 }
num[6] ={ 'S':1,'I':1,'X':1 }
num[7] ={ 'S':1,'E':2,'V':1,'N':1 }
num[8] ={ 'E':1,'I':1,'G':1,'H':1,'T':1 }
num[9] ={ 'N':2,'I':1,'E':1 }
even = {0:'Z',2:'W',4:'U',6:'X',8:'G'}
odd = {1:'O',3:'T',5:'F',7:'S'}

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  letterpool = {}
  digits = []
  ss = raw_input()
  for letter in ss:
    if letter in letterpool:
      letterpool[letter] = letterpool[letter] + 1 
    else:
      letterpool[letter] = 1
  for digit in even:
    if (even[digit] in letterpool):
      while (letterpool[even[digit]] > 0):
        digits.append(digit)
        for l in num[digit]:
          letterpool[l] = letterpool[l] - num[digit][l]
  for digit in odd:
    if (odd[digit] in letterpool):
      while (letterpool[odd[digit]] > 0):
        digits.append(digit)
        for l in num[digit]:
          letterpool[l] = letterpool[l] - num[digit][l]
  if ('E' in letterpool):
    while (letterpool['E'] > 0):
      digits.append(9)
      letterpool['E'] = letterpool['E'] - 1
  digits.sort()
  digits_s = ["%d" %n for n in digits]
  res = "".join(digits_s)
  case_str = "Case #%d: " %i
  print case_str + res
