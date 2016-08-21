import fs

def solve(input):
  occured = {}
  for letter in range(10):
    occured[str(letter)] = False
  j = 0
  for i in range(100000):
    j+=1
    multiple_input = str(int(input) * j)
    for letter in multiple_input:
      occured[letter] = True
    reached_goal = True
    for letter in occured:
      if not occured[letter]:
        reached_goal = False
        break
    if reached_goal:
      break
  output = multiple_input
  if not reached_goal:
    output = 'INSOMNIA'
  return output

if __name__ == '__main__':
  IN_NAME = 'input.txt'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  for i, row in enumerate(rows):
    # Skip first row (contains number of entries)
    if i == 0: continue
    # Skip last row (contains only \n)
    if i == len(rows) - 1: continue
    solution += 'Case #%i: %s\n' % (i, str(solve(row)))

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)