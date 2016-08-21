filename = raw_input('Enter the filename: ')

#################
# Timing
import time
start = time.time()

# Opening file
defaultfn = 'b-init.in'
try:
  if len(filename) == 0:
    fi = open(defaultfn)
    filename = defaultfn
  else:
    fi = open(filename)
except:
  print "File cannot be opened", filename
  exit()

#################
# Solution.
testCases = int(fi.readline())
results = []

def signsToNums(line):
  return line.replace('-','0').replace('+','1')

def numsToSigns(line):
  return line.replace('0','-').replace('1','+')

def opposite(line):
  return line.replace('-','0').replace('+','-').replace('0','+')

def flipTop(stack, num): 
  return list(opposite(reversed(stack[:num]))) + list(stack[num:])

def removeDuplicates(stack): 
  while ('++' in stack) or ('--' in stack):
    stack = stack.replace('++','+').replace('--','-')
  return stack

for x in xrange(0, testCases):
  result = -1
  # New case
  casetime = time.time()
  case = str(x+1)
  line = fi.readline().rstrip()
  # print line, signsToNums(line)
  
  line = removeDuplicates(line)

  if line == "+":
    result = 0
  elif line[-1] == "+":
    result = len(line) - 1
  else:
    result = len(line)

  print "Case",case,"time:", str(time.time() - casetime), "sec"

  caseLine = "Case #" + case
  results.append(caseLine + ": " + str(result))
  

print '\n'.join(results)

#################
# Output file.
name = filename.split('.')[0]
fo = open(name + '.out', 'w')
fo.write('\n'.join(results))

fi.close()
fo.close()

print "Total time:", str(time.time() - start), "sec"