def find_steps(S):
  pancakes = [1 if c == '+' else 0 for c in S]
  # start with rightmost '-'
  j = len(pancakes) - 1
  steps = 0
  
  # find rightmost 0, everything from the left to that will need to be flipped
  while j >= 0 and pancakes[j] == 1:
    j -= 1
    
  # if all are 0
  if j == -1:
    return 0
  
  if j == 0:
    return 1
  
  while j >= 0:
    # find leftmost 0 and flip all of them
    i = 0
    while i != j and pancakes[i] == 1:
      i += 1
    if i > 0:
      # flip all the ones from 0 to i
      pancakes = flip(i, pancakes)
      steps += 1
    
    pancakes = flip(j + 1, pancakes)
    steps += 1
    
    while j >= 0 and pancakes[j] == 1:
      j -= 1
  
  return steps
  
def flip(stop, pancakes):
  return [1 if c == 0 else 0 for c in pancakes[:stop][::-1]] + pancakes[stop:]
  
T = int(raw_input())
for i in xrange(T):
  S = raw_input().strip()
  print "Case #%d: %d" % (i + 1, find_steps(S))