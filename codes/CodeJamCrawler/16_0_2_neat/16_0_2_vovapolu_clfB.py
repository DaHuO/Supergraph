fin = open('input.txt', 'rb')
fout = open('output.txt', 'wb')

n = int(fin.readline()[:-1])
for i in xrange(n):
  s = fin.readline()[:-1]
  cur_ans = 0

  j = 0
  while True:
    while j < len(s) and s[j] == '+':
      j += 1

    if j > 0 and j < len(s):
      cur_ans += 1

    if j == len(s):
      break

    while j < len(s) and s[j] == '-':
      j += 1
    cur_ans += 1

  fout.write('Case #{}: {}\n'.format(i + 1, cur_ans))



