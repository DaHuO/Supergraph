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
results = list()


for x in xrange(0, testCases):
  # New case
  casetime = time.time()
  case = str(x+1)
  caseLine = "Case #" + case
  print caseLine
  n = int(fi.readline().rstrip())

  tmp = list()
  for line in xrange(0, 2*n-1):
    tmp += map(int, fi.readline().rstrip().split())
  tmp.sort()

  tmpResult = list()
  count = 0
  current = tmp[0]
  for x in tmp:
    if (x != current):
      if (count % 2 != 0):
        tmpResult.append(current)
      count = 1
      current = x
    else:
      count += 1

  if (len(tmpResult) == n-1):
    tmpResult.append(tmp[-1])

  # print tmp

  tmpResult = map(str, tmpResult)
  # tmpResult.sort()

  results.append(caseLine + ": " + ' '.join(tmpResult))
  # exit()

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