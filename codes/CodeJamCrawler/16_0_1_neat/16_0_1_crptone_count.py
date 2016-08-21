f = open('count-large.in')
g = open('count.out', 'w')
lines = f.readlines()
for i in range(1,len(lines)):
  n = int(lines[i].strip())
  if int(n) == 0:
    g.write('Case #' + str(i) + ': INSOMNIA\n')
    continue
  nums = set()
  c = n
  while True:
   # print(nums)
    nums |= set(str(c))
    if len(nums) == 10:
      break
    c += n
  g.write('Case #' + str(i) + ': ' + str(c) + '\n')
  #print('*****')

f.close()
g.close()
