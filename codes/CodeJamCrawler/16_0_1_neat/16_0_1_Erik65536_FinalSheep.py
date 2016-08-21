import sys

ORD_0 = ord('0')

def GetLastSheep(n_0):
  if n_0 <= 0:
    return "INSOMNIA"
  seen = [False]*10
  n_x = n_0
  while True:
    for char in str(n_x):
      seen[ord(char) - ORD_0] = True
    if all(seen):
      return str(n_x)
    n_x += n_0

cases = []
with open(sys.argv[1]) as file:
  tests = int(file.readline())
  for test in range(tests):
    cases.append(int(file.readline()))

for index, case in enumerate(cases):
  last = GetLastSheep(case)
  print("Case #%d: %s" % (index+1, last))
