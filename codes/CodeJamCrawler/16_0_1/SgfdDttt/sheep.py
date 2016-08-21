input_file = "A-large.in"
counter = -1
for line in open(input_file, 'r'):
  counter += 1
  if counter == 0:
    continue
  N = int(line)
  if N == 0:
    print("Case #" + str(counter) + ": INSOMNIA")
    continue
  numbers = dict()
  for i in range(10):
    numbers[i] = 0
  done = False
  acc = N
  while (not done):
    for int_str in str(acc):
      numbers[int(int_str)] = 1
    done = True
    for i in range(10):
      done = (numbers[i] == 1) and done
    acc += N
  acc -= N
  print("Case #" + str(counter) + ": " + str(acc))
