in_file = "A-large(1).in"
counter = -1

for line in open(in_file, 'r'):
  counter += 1
  if counter == 0:
    continue
  all_digits = list()
  line = line.replace('\n', '')
  while 'Z' in line:
    line = line.replace('Z', '', 1)
    line = line.replace('E', '', 1)
    line = line.replace('R', '', 1)
    line = line.replace('O', '', 1)
    all_digits.append(0)
  while 'W' in line:
    line = line.replace('T', '', 1)
    line = line.replace('W', '', 1)
    line = line.replace('O', '', 1)
    all_digits.append(2)
  while 'X' in line:
    line = line.replace('S', '', 1)
    line = line.replace('I', '', 1)
    line = line.replace('X', '', 1)
    all_digits.append(6)
  while 'G' in line:
    line = line.replace('E', '', 1)
    line = line.replace('I', '', 1)
    line = line.replace('G', '', 1)
    line = line.replace('H', '', 1)
    line = line.replace('T', '', 1)
    all_digits.append(8)
  while 'U' in line:
    line = line.replace('F', '', 1)
    line = line.replace('O', '', 1)
    line = line.replace('U', '', 1)
    line = line.replace('R', '', 1)
    all_digits.append(4)
  while 'H' in line:
    line = line.replace('T', '', 1)
    line = line.replace('H', '', 1)
    line = line.replace('R', '', 1)
    line = line.replace('E', '', 2)
    all_digits.append(3)
  while 'F' in line:
    line = line.replace('F', '', 1)
    line = line.replace('I', '', 1)
    line = line.replace('V', '', 1)
    line = line.replace('E', '', 1)
    all_digits.append(5)
  while 'O' in line:
    line = line.replace('O', '', 1)
    line = line.replace('N', '', 1)
    line = line.replace('E', '', 1)
    all_digits.append(1)
  while 'V' in line:
    line = line.replace('S', '', 1)
    line = line.replace('E', '', 2)
    line = line.replace('V', '', 1)
    line = line.replace('N', '', 1)
    all_digits.append(7)
  while 'I' in line:
    line = line.replace('N', '', 2)
    line = line.replace('I', '', 1)
    line = line.replace('E', '', 1)
    all_digits.append(9)
  all_digits.sort()
  answer_str = ''
  for i in all_digits:
    answer_str = answer_str + str(i)
  print('Case #' + str(counter) + ': ' + answer_str)
