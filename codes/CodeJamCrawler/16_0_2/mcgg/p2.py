__author__ = 'zhaokaihao'

class p2(object):
  def count_flip(self, cakes):
    current = cakes[0]
    count = 0
    for i in range(1, len(cakes)):
      if cakes[i] == current:
        continue
      else:
        count += 1
        current = cakes[i]
    if cakes[-1] == '-':
      count += 1
    return str(count)


file = open('input.txt')
n = int(file.readline())
output = open('output.txt', 'w')

for i in range(1, n+1):
  cakes = file.readline().split()[0]
  obj = p2()
  output.write('Case #' + str(i) + ': ' + obj.count_flip(cakes) + '\n')
