import sys
def lastNumber(startNumber):
  if startNumber == 0:
    return "INSOMNIA"
  numbersSeen = set()
  orig = long(startNumber)
  while len(numbersSeen) < 10:
    number = startNumber
    #print "Adding digits for ", startNumber
    while number > 0:
      #print "Adding digit ", number%10
      numbersSeen.add(number%10)
      number /= 10
    if len(numbersSeen) >= 10:
      break
    startNumber += orig 
  return str(startNumber)

#print lastNumber(0)
#print lastNumber(1)
#print lastNumber(2)
#print lastNumber(11)
#print lastNumber(1692)
#print lastNumber(1234567890)
#print lastNumber(1000)
#for n in range(1000001):
  #if n%1000 == 0:
    #print "Testing n: ", n
  #x = lastNumber(n)

#print lastNumber(1234)

inlines = open(sys.argv[1]).readlines()
numcases = int(inlines[0])
idx = 1

for case in range(numcases):
    num = int(inlines[idx])
    print "Case #%d: %s" % (case + 1, lastNumber(num) )
    idx += 1


