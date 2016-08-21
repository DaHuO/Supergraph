def isHappy(stack) :
  for p in stack :
    if chr(p) == '-' :
      return False
  return True

def flipI(stack, pos, p) :
  hold = '+' if chr(stack[pos]) == '-' else '-';
  stack[pos] = '+' if chr(stack[p]) == '-' else '-';
  stack[p] = hold;

def flip(stack) :
  flipping = False
  pos = 0
  for p in reversed(range(len(stack))) :
    if flipping :
      if pos <= p :
        flipI(stack, pos, p)
        pos += 1
      else :
        break
    elif chr(stack[p]) == '-':
      flipping = True
      flipI(stack, pos, p)
      pos += 1


t = input()
for i in range(1,t+1) :
  stack = bytearray(raw_input())
  print "Case #{}:".format(i),
  step = 0
  while not isHappy(stack) :
    if chr(stack[0]) == '+' :
      for j in range(len(stack)) :
        if chr(stack[j]) == '+' :
          stack[j] = '-'
        else:
          break
    else :
      flip(stack)
    step += 1
  print step
