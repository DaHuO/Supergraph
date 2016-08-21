input_file = "B-large.in"
counter = -1
for line in open(input_file, 'r'):
  counter += 1
  if counter == 0:
    continue
  flips = 0
  stack = line.replace("\n", "")
  if stack[len(stack)-1] == '-':
    flips+=1
  for i in range(1,len(stack)):
    if not (stack[i-1] == stack[i]):
      flips+=1
  answer_str = "Case #" + str(counter) + ": "
  answer_str += str(flips)
  print answer_str
