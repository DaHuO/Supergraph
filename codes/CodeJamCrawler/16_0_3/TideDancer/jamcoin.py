import math
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = input()  # read a line with a single longeger
for i in range(1, t + 1):
  N,J = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}:".format(i))

  t = 0
  for middle in range(0, 2**N):
    
    s = '1'+bin(middle)[2:].zfill(N-2)+'1'
    divisor_list = []

    for base in range(2,11):
      num = long(s, base)
      for p in range(2,long(round(math.sqrt(num)))):
        if num % p == 0:
          divisor_list.append(str(p))
          break
    if len(divisor_list) == 9:
      print('{} {}'.format(s, ' '.join(divisor_list)))
      t = t + 1
    if t == J:
      break
     

