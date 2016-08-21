fin = open('B-large.in', 'r')
fout = open('out.txt', 'w')
C = -1
for line in fin:
  C += 1
  if C == 0:
    T = int(line)
    continue
  fout.write('Case #{}: '.format(C))
  n = len(line)
  f = [[0 for j in range(2)] for i in range(n)]
  if line[0] == '-':
    f[0][0] = 0
    f[0][1] = 1
  else:
    f[0][0] = 1
    f[0][1] = 0
  for i in range(1, n):
    if line[i] == '-':
      f[i][0] = f[i - 1][0]
      f[i][1] = f[i - 1][0] + 1
    else :
      f[i][0] = f[i - 1][1] + 1
      f[i][1] = f[i - 1][1]
  fout.write('{}\n'.format(f[n - 1][1]))