def calculateMove(a, b):
  if a=='-':
    if b=='-':
      return (1, '+')
    else:
      return (0, '-')
  else:
    if b=='-':
      return (2, '+')
    else:
      return (0, '+')

def flip(i, pancakes):
  newPancakes = list(pancakes)

  j=0
  while i>=0:
    if pancakes[i]=='-':
      newPancakes[j] = '+'
    else:
      newPancakes[j] = '-'
    i = i-1
    j = j+1

  return newPancakes

def makeMove(top, i, pancakes):
  pancakes[i] = '+'
  pancakes[0] = top
  newPancakes = list(pancakes)

  i=i-1
  j=1
  while i>0:
    if pancakes[i]=='-':
      newPancakes[j] = '+'
    else:
      newPancakes[j] = '-'
    i = i-1
    j = j+1

  return newPancakes


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for icase in xrange(1, t + 1):
  s, = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  result = 0

  # print "   - Starting Case # {}".format(icase)

  pancakes = list(s)
  i = len(s)-1
  while i>=0:
    currentState = list(pancakes)

    move = calculateMove(pancakes[0], pancakes[i])
    result = result + move[0]

    if move[0]==1:
      pancakes = flip(i, pancakes)
    elif move[0]==2:
      count = 0
      j=0
      while pancakes[j]==pancakes[0]:
        count = count+1
        j=j+1
      # print "     - Cortaremos primero en: {}".format(count)
      pancakes = flip(count-1, pancakes)
      # print "     - {}".format(pancakes)
      pancakes = flip(i, pancakes)

    # print "   - Testing: {} -> {} ( sumar {} ({}) )".format(currentState, pancakes, move[0], result)

    i = i-1

  print "Case #{}: {}".format(icase, result)
  # check out .format's specification for more formatting options

