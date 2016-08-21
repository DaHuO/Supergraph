fin = open('A-large.in', 'r')
fout = open('out.txt', 'w')
i = -1
for line in fin:
  i += 1
  if i == 0:
    t = int(line)
    continue
  fout.write('Case #{}: '.format(i))
  n = int(line)
  #print 'n = ', n
  if n == 0:
    fout.write('INSOMNIA\n')
    continue
  ok = [0] * 10
  j = 1
  ans = n
  while not ok == ([1] * 10):
    ans = n * j
    tmp = n * j
    while tmp > 0:
      ok[tmp % 10] = 1
      tmp /= 10
    j += 1
  fout.write('{}\n'.format(ans))
fin.close()
fout.close()
  
  
  