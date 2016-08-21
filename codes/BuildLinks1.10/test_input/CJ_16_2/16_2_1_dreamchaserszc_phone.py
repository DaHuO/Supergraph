from collections import defaultdict
import fileinput

class TestCase(object):
  def __init__(self, s):
    self.s = s

def solve(t):

  character_list = list(t.s.strip())

  list1 = [226, 376, 298, 385, 298]

  table = defaultdict(lambda: 0)
 
  for x in character_list:
    table[x] = table[x] + 1 

  phone_num = ''

  #for 0, 2, 4, 6, 8
  if table['Z'] != 0:
    count = table['Z']
    for i in range(count):
      phone_num = phone_num + '0'
    table['Z'] = 0
    table['E'] = table['E'] - count
    table['R'] = table['R'] - count
    table['O'] = table['O'] - count

  if table['W'] != 0:
    count = table['W']
    for i in range(count):
      phone_num = phone_num + '2'
    table['W'] = 0
    table['T'] = table['T'] - count
    table['O'] = table['O'] - count
  
  if table['U'] != 0:
    count = table['U']
    for i in range(count):
      phone_num = phone_num + '4'
    table['U'] = 0
    table['F'] = table['F'] - count
    table['R'] = table['R'] - count
    table['O'] = table['O'] - count
    print table
  
  if table['X'] != 0:
    count = table['X']
    for i in range(count):
      phone_num = phone_num + '6'
    table['X'] = 0
    table['I'] = table['I'] - count
    table['S'] = table['S'] - count
  
  if table['G'] != 0:
    count = table['G']
    for i in range(count):
      phone_num = phone_num + '8'
    table['G'] = 0
    table['I'] = table['I'] - count
    table['E'] = table['E'] - count
    table['H'] = table['H'] - count
    table['T'] = table['T'] - count

  if table['O'] != 0:
    count = table['O']
    for i in range(count):
      phone_num = phone_num +'1'
    table['O'] = 0
    table['N'] = table['N'] - count
    table['E'] = table['E'] - count

  if table['T'] != 0:
    count = table['T']
    for i in range(count):
      phone_num = phone_num + '3'
    table['T'] = 0
    table['H'] = table['H'] - count
    table['R'] = table['R'] - count
    table['E'] = table['E'] - (count *2)

  if table['F'] != 0:
    count = table['F']
    for i in range(count):
      phone_num = phone_num + '5'
    table['F'] = 0
    table['I'] = table['I'] - count
    table['V'] = table['V'] - count
    table['E'] = table['E'] - count

  if table['S'] != 0:
    count = table['S']
    for i in range(count):
      phone_num = phone_num + '7'
    table['S'] = 0
    table['N'] = table['N'] - count
    table['V'] = table['V'] - count
    table['E'] = table['E'] - (count * 2)

  if table['N'] != 0:
    count = table['N'] / 2
    for i in range(count):
      phone_num = phone_num + '9'
    table['N'] = 0
    table['I'] = table['I'] - count
    table['E'] = table['E'] - count

  ascii_sum = 0
  for x in table.keys():
    if table[x] != 0:
      temp_sum = 0
      for y in list(x):
        temp_sum = temp_sum + ord(y)
      
      ascii_sum = ascii_sum + temp_sum * table[x]

  print ascii_sum
  phone_num = ''.join(sorted(phone_num))

  if (ascii_sum != 0):
    print table, t.s.strip(), phone_num

  return phone_num

start = True
i = 0
numberOfT = 0
testCases = []

for line in fileinput.input():
  if start:
    numberOfT = int(line)
    start = False
    continue
    
  t = TestCase(line)
  testCases.append(t)

i = 1
f = open('answer', 'w')
for t in testCases:
  answer = solve(t)
  f.write("Case #" + str(i) + ": " + str(answer) + "\n")
  i = i + 1


