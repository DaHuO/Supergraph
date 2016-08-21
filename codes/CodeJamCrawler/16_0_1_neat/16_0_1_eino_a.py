import sys

def sheep_count(n):
  t = 0;
  digits = []
  tmp_n = n
  if n == 0:
    return "INSOMNIA"
  while (True):
    if '0' in str(tmp_n) and 0 not in digits:
      digits.append(0)
    if '1' in str(tmp_n) and 1 not in digits:
      digits.append(1)
    if '2' in str(tmp_n) and 2 not in digits:
      digits.append(2)
    if '3' in str(tmp_n) and 3 not in digits:
      digits.append(3)
    if '4' in str(tmp_n) and 4 not in digits:
      digits.append(4)
    if '5' in str(tmp_n) and 5 not in digits:
      digits.append(5)
    if '6' in str(tmp_n) and 6 not in digits:
      digits.append(6)
    if '7' in str(tmp_n) and 7 not in digits:
      digits.append(7)
    if '8' in str(tmp_n) and 8 not in digits:
      digits.append(8)
    if '9' in str(tmp_n) and 9 not in digits:
      digits.append(9)
    if len(digits) == 10:
      return tmp_n
    t += 1
    tmp_n = t*n

n = sys.stdin.readline()
cnt = 1

for line in sys.stdin:
  t = sheep_count(int(line))
  print ("Case #" + str(cnt) + ": " + str(t))
  cnt += 1
