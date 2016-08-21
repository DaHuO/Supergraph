from random import *
from math import sqrt
class p3(object):

  code_lib = []

  def __init__(self):
    self.code_lib = []

  def basex(self, x, code):
    rs = 0
    code = code[::-1]
    for i in range(len(code)):
      rs += int(code[i]) * (x ** i)
    if self.is_prime(int(rs)):
      return '-1'
    else:
      return rs

  def get_inter(self, code):
    rs = []
    for item in range(2, 10):
      temp = self.basex(item, code)
      if temp == '-1':
        return False
      rs.append(temp)
    if self.is_prime(int(code)):
      return False
    else:
      rs.append(int(code))
    return rs

  def mrange(self, start, stop, step):
    while start < stop:
        yield start
        start += step

  def is_prime(self, num):
      if num == 2:
          return True
      if (num < 2) or (num % 2 == 0):
          return False
      return all(num % i for i in self.mrange(3, int(sqrt(num)) + 1, 2))

  def get_non_divisor(self, val):
    curr_i = 2
    while curr_i < val:
      if val % curr_i == 0:
        return curr_i
      curr_i += 1

  def generate_code(self, len):
    len -= 2
    rs = ''
    while (rs=='') or (rs in self.code_lib):
      rand = lambda n: [randint(0,1) for b in range(1,n+1)]
      sub_rs = ''.join(str(e) for e in rand(len))
      rs = '1'+ sub_rs +'1'
    self.code_lib.append(rs)
    return rs


file = open('input.txt')
t = int(file.readline())
output = open('output.txt', 'w')
c = 0

for i in range(1, t+1):
  line = file.readline()
  n = line.split()[0]
  j = line.split()[1]
  obj = p3()
  output.write('Case #' + str(i) + ':\n')
  t = int(j)
  while t > 0:
    result = []
    code = obj.generate_code(int(n))
    inter = obj.get_inter(code)
    if not inter:
      continue
    else:
      t -= 1
    for x in inter:
      result.append(obj.get_non_divisor(x))
    result2 = ' '.join(str(e) for e in result)
    output.write(code+' '+result2 + '\n')


