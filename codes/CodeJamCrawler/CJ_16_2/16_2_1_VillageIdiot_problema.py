import sys
from collections import deque

firstChars = ['Z','O','T','F','S','E','N']
wordToDigit = {'ZERO':'0', 'ONE':'1','TWO':'2', 'THREE':'3', 'FOUR':'4', 'FIVE':'5', 'SIX':'6', 'SEVEN':'7', 'EIGHT':'8', 'NINE':'9'}

  
def doTest(line):
  allChars = line
  q = deque()
  for idx in range(len(allChars)):
    q.append((allChars[idx]+allChars[:idx] + allChars[idx+1:],'',''))

  solutions = []
  while len(q) > 0:
    remainingCs, workingWord,workingDigits = q.pop()
    if len(remainingCs) == 0:
      return "".join([x for x in sorted(workingDigits)])
    if len(workingWord) == 0:
      if remainingCs[0] in firstChars:
        for idx in range(len(remainingCs[1:])):
          remainingChars = remainingCs[1:][idx] + remainingCs[1:][:idx] + remainingCs[1:][idx+1:]
          q.append((remainingChars, remainingCs[0], workingDigits)) 
    else:
      newWord = workingWord+remainingCs[0]
      if newWord in wordToDigit:
        if len(remainingCs[1:]) == 0:
          q.append(('','',workingDigits+wordToDigit[newWord]))
        else:
          for idx in range(len(remainingCs[1:])):
            q.append( (remainingCs[1:][idx] + remainingCs[1:][:idx]+remainingCs[1:][idx+1:], '', workingDigits + wordToDigit[newWord]) )
      else:
        for w in wordToDigit.keys():
          if w.find(newWord) == 0:
            for idx,v in enumerate(remainingCs[1:]):
              q.append( (remainingCs[1:][idx] + remainingCs[1:][:idx]+remainingCs[1:][idx+1:], newWord, workingDigits) )
  return ""
  

inlines = open(sys.argv[1]).readlines()
numcases = int(inlines[0])
idx = 1

for case in range(numcases):
    s = doTest(inlines[idx].rstrip('\n'))
    print "Case #%d: %s" % (case + 1, s)
    idx += len(s.split('\n'))


