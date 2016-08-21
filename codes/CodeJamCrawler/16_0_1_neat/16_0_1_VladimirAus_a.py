filename = raw_input('Enter the filename: ')

#################
# Timing
import time
start = time.time()

# Opening file
defaultfn = 'a-init.in'
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


for x in xrange(0, testCases):
  # New case
  casetime = time.time()
  case = str(x+1)
  print "Case:", case
  n = int(fi.readline().rstrip())
  
  # New Case
  sawThat = list()
  y = 1
  while True:
    sawThat = list(set(list(tuple(list(str(n*y)))) + sawThat))

    caseLine = "Case #" + case
    if n == 0:
      results.append(caseLine + ": INSOMNIA")
      break
    elif len(sawThat) == 10:
      results.append(caseLine + ": " + str(n*y))
      break

    y += 1

  print "Case time:", str(time.time() - casetime), "sec"
  

print '\n'.join(results)

#################
# Output file.
name = filename.split('.')[0]
fo = open(name + '.out', 'w')
fo.write('\n'.join(results))

fi.close()
fo.close()

print "Total time:", str(time.time() - start), "sec"