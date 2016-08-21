# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def isAtLeastOneZero(someArray):
    for element in someArray:
        if element ==0:
            return True
    return False

def updateArray(someArray, m):
    strM = str(m)
    for digit in strM:
        someArray[int(digit)]+=1
    return someArray

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    array = [0]*10
    n = int(raw_input())
    originalValue=n
    multiplier = 1
    while isAtLeastOneZero(array) and n!=0:
        array=updateArray(array, n)
        multiplier+=1
        n=originalValue*multiplier
    if n==0:
        print "Case #"+str(i)+": INSOMNIA"
    else:
        print "Case #"+str(i)+": "+str(originalValue*(multiplier-1))
 
  # check out .format's specification for more formatting options