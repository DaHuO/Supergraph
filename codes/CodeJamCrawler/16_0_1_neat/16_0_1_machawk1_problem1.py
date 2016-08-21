import sys

inputFile = sys.argv[1]

file = open(inputFile)
txt = file.read()
lines = txt.split('\n')

testCaseCount = lines.pop(0)

for idx,val in enumerate(lines):
  if len(val) == 0:continue
  digitsMet = 0
  digitsM = [False] * 10
  multiple = 1
  repeatThreshold = 0 #check if no new number have come up to prevent infinite loops and report 'insomnia'
  while digitsMet <= 10 and repeatThreshold < 10000000:
    valAsInt = str(int(val.strip()) * multiple)
    #print valAsInt
    for letter in valAsInt:
      if not digitsM[int(letter)]:
        digitsM[int(letter)] = True
        digitsMet += 1
        repeatThreshold = 0
        #print letter+" found"+ str(digitsMet)
        if digitsMet >= 10: break
      else:
        repeatThreshold += 1
    if digitsMet >= 10: break
    multiple += 1

  if digitsMet < 10:
    print "Case #"+str(idx+1)+": INSOMNIA"
  else:
    print "Case #"+str(idx+1)+": "+str(int(val) * multiple)
    
file.close()