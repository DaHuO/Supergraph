__author__ = 'zhaokaihao'

class p1(object):
  rs = [0] * 10
  count = 0
  def __init__(self):
    self.rs = [0] * 10
    self.count = 0
  def fill_rs(self, s):
    x = 1
    while True:
      number  = str(int(s)*x)
      x += 1
      for i in range(len(number)):
        if number[i] in self.rs:
          continue
        else:
          self.rs[int(number[i])] = number[i]
          self.count += 1
        if self.count == 10:
          return number



file = open('input.txt')
n = int(file.readline())
output = open('output.txt', 'w')

for i in range(1, n+1):
  num = file.readline().split()[0]
  obj = p1()
  if num == '0':
    output.write('CASE #' + str(i) + " INSOMNIA\n")
  else:
    output.write('CASE #' + str(i) + ' ' + obj.fill_rs(num) + '\n')

