

import sys


def solveIt(s):
  maxletter = ''
  word = ''

  index = 0
  slen = len(s)
  while (index < slen):
    print 'm: ' + maxletter + ' s[index]:' + s[index] + ' word: '+word
    if (s[index] >= maxletter):
      maxletter = s[index]
      word = maxletter + word
    else:
      word = word + s[index]
    index += 1
  print 'word is '+word
  return word
  



# actually process the solution file
with open(sys.argv[1]) as file:
  with open("ans_"+sys.argv[1],'w') as outFile:
    lines = file.read().splitlines()

    count = -1
    for line in lines:
      # skip the test count line
      count += 1
      if (count == 0):
        continue

      result = solveIt(line)

      outFile.write('Case #'+str(count)+': '+str(result))
      outFile.write('\n')