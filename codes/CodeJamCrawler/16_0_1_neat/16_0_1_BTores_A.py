sleepNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def checkSleep():
    for i in sleepNumbers:
        if( i == 0 ):
            return False
    return True

def breakdownNumber(n):
    n = str(n)
    for c in n:
        sleepNumbers[int(c)] = 1
    
def solve( case ):
    case = int(case)
    if (case == 0):
        return "INSOMNIA"
    n = 1;
    while True:
        breakdownNumber(case*n)
        if( checkSleep()):
            return n*case
        n = n + 1
    
caseNumbers = input()
for caseN in xrange(1, caseNumbers+1):
    sleepNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    case = raw_input()
    print("Case #%i: %s" % (caseN, solve(case)))
