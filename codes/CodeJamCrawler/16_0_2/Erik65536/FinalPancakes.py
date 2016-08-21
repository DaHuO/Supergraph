import sys

def FlipPancakes(pancakes, i):
  for index in range(i):
    pancakes[index] = not pancakes[index]
  if i >= 2:
    pancakes[:i] = pancakes[i-1::-1]
  return pancakes

def SolvePancakes(pancakes):
  count = 0
  while not all(pancakes):
    if pancakes[0]:
      i = pancakes.index(False)
    else:
      i = len(pancakes) - pancakes[::-1].index(False)
    pancakes = FlipPancakes(pancakes, i)
    count += 1
  return count

cases = []
with open(sys.argv[1]) as file:
  tests = int(file.readline())
  cases = [None]*tests

  for test in range(tests):
    line = file.readline().strip()
    pancakes = [False]*len(line)
    for index in range(len(line)):
      pancakes[index] = line[index] == '+'
    cases[test] = pancakes

for index, case in enumerate(cases):
  n = SolvePancakes(case)
  print("Case #%d: %s" % (index+1, n))
