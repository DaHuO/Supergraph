def isValidStack(stack):
  for ch in stack:
    if ch != '+':
      return False
  return True

def smartFlip(stack):
  start = 0
  end = None
  if stack[0] == '+':
    end = 0 
    while (end < len(stack)) and (stack[end] == '+'):
      end += 1
  else:
    end = len(stack)
    while (end > 0) and (stack[end-1] == '+'):
      end -= 1
  stack[start:end] = reversed(stack[start:end])
  for i in range(start, end):
    if stack[i] == '+':
      stack[i] = '-'
    else:
      stack[i] = '+'

stacks = []
with open("input.txt", "r") as inputFile:
  inputFile.readline()
  for line in inputFile:
    stacks.append(list(line.rstrip('\n')))

with open("output.txt", "w") as outputFile:
  case = 1
  for stack in stacks:
    count = 0
    while not isValidStack(stack):
      smartFlip(stack)
      count += 1
    outputFile.write("Case #{}: {}\n".format(case, count))
    case += 1
