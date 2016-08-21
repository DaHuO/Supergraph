import os

def solve_n(n):
  if n == 0:
    return 'INSOMNIA'

  seen = set()

  i = 1
  while True:
    temp_n = n * i
    while temp_n > 0:
      seen.add(temp_n % 10)
      temp_n /= 10
    if len(seen) == 10:
      return n * i
    i += 1

fin = open('A-large.in', 'r')
fout = open('A.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  n = int(line)

  res = solve_n(n)

  out_str = 'Case #%d: %s' % (i, res)
  print out_str
  fout.write(out_str + '\n')
fin.close()
fout.close()
