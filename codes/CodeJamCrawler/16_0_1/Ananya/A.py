from operator import mul
import fileinput

case = -1
for line in fileinput.input():
  case += 1
  if case == 0:
    continue
  number = int(line)
  seen = [0]*10
  cur_number = 0
  if number == 0:
    print("Case #%d: INSOMNIA" % case)
  else:
    while reduce(mul, seen, 1) == 0:
      cur_number += number
      digits = list(str(cur_number))
      for d in digits:
        seen[(int(d))] = 1
    print("Case #%d: %d" % (case, cur_number))
