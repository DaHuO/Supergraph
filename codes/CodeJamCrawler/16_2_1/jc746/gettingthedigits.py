#! /usr/bin/env python
import sys

if len(sys.argv) < 2:
  print "Please give me an input file."
  sys.exit(1)

input_file = open(sys.argv[1], 'r')
test_count = int(input_file.readline())

if len(sys.argv) < 3:
  output = sys.stdout
  print "Not given output file, writing to stdout."
else:
  output = open(sys.argv[2], 'w')
  print "Writing to '%s'" % sys.argv[2]

for test_case in range(1, test_count + 1):
  line = input_file.readline().strip()
  result = []
  data = sorted(list(line))
  while 'Z' in data:
    result.append(0)
    data.remove('Z')
    data.remove('E')
    data.remove('R')
    data.remove('O')
  while 'W' in data:
    result.append(2)
    data.remove('T')
    data.remove('W')
    data.remove('O')
  while 'X' in data:
    result.append(6)
    data.remove('S')
    data.remove('I')
    data.remove('X')
  while 'G' in data:
    result.append(8)
    data.remove('E')
    data.remove('I')
    data.remove('G')
    data.remove('H')
    data.remove('T')
  while 'U' in data:
    result.append(4)
    data.remove('F')
    data.remove('O')
    data.remove('U')
    data.remove('R')
  while 'F' in data:
    result.append(5)
    data.remove('F')
    data.remove('I')
    data.remove('V')
    data.remove('E')
  while 'V' in data:
    result.append(7)
    data.remove('S')
    data.remove('E')
    data.remove('V')
    data.remove('E')
    data.remove('N')
  while 'R' in data:
    result.append(3)
    data.remove('T')
    data.remove('H')
    data.remove('R')
    data.remove('E')
    data.remove('E')
  while 'O' in data:
    result.append(1)
    data.remove('O')
    data.remove('N')
    data.remove('E')
  while len(data) > 0:
    result.append(9)
    data.remove('N')
    data.remove('I')
    data.remove('N')
    data.remove('E')


  output.write('Case #%d: ' % test_case)
  output.write(''.join(map(str, sorted(result))))
  output.write('\n')
