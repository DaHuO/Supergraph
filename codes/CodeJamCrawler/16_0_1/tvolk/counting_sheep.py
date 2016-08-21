import sys

def countNumSeen(value):
  originalval = value
  unseenlist = [0,1,2,3,4,5,6,7,8,9]
  lastlistsize = len(unseenlist)
  count = 1
  while True:
    unseenlist = checkIfSeen(value, unseenlist)
    if len(unseenlist) > 0:
      value = formula(count, originalval)
    if len(unseenlist) == 0:
      break
    if count > 1 and originalval == value:
      return 'INSOMNIA'
    count += 1
  return value

def checkIfSeen(value, unseenlist):
  for digit in str(value):
    if int(digit) in unseenlist:
      unseenlist.remove(int(digit))
  return unseenlist

def formula(index, value):
  return index * value

def testCase(index, case):
  result = countNumSeen(case)
  print 'Case #%d: %s' %(index, result)

inputlist = [int(line.strip()) for line in sys.stdin]
num_of_tests = inputlist[0]

for index, case in enumerate(inputlist[1:], start=1):
  testCase(index, case)
