import math
import sys

def GetStudentTiles(length, complexity, students):
  GOLD = [True]*length
  min_students = math.ceil(length / complexity)
  if students < min_students:
    return None
  students = []

  gold_start = 0
  while gold_start < length:
    start = []
    gold_end = min(gold_start + complexity, length)
    for gold in range(gold_start, gold_end):
      start_gold = [False]*length
      start_gold[gold] = True
      start.append(start_gold)
    gold_start = gold_end
    student = GetStudent(1, complexity, 0, length, start, start, GOLD)
    students.append(student)
  return students

def GetStudent(k, complexity, position, length, start, previous, GOLD):
  fractiles = len(start)

  if k == complexity:
    for tile in range(length):
      all_gold = True
      for fractile in range(fractiles):
        all_gold &= previous[fractile][tile]
      if all_gold:
        return position + tile + 1
    return None

  current = [None]*fractiles
  for tile in range(length):
    ngold = 0
    for fractile in range(fractiles):
      if previous[fractile][tile]:
        current[fractile] = GOLD
        ngold += 1
      else:
        current[fractile] = start[fractile]
    if ngold < min(k, fractiles):
      continue
    student = GetStudent(k+1, complexity, (position+tile)*length, length, start, current, GOLD)
    if student is not None:
      return student
  return None

cases = []
with open(sys.argv[1]) as file:
  tests = int(file.readline())
  solutions = []

  for test in range(tests):
    line = file.readline().strip().split(' ')
    length = int(line[0])
    complexity = int(line[1])
    students = int(line[2])
    solution = GetStudentTiles(length, complexity, students)
    if solution is None:
      solution = "IMPOSSIBLE"
    else:
      solution = ' '.join([str(x) for x in solution])
    solutions.append(solution)

for index, solution in enumerate(solutions):
  print("Case #%d: %s" % (index+1, solution))
