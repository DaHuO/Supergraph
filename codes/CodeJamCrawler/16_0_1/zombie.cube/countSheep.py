def check(seen):
    return len(seen) is 10

def addDigitsToSet(n, seen):
    while n:
        d = n % 10
        seen.add(d)
        n //= 10

def printOutput(i, result):
    print ('Case #' + str(i) + ': ' + str(result))
    
def countSheep(n, seen):
    if n == 0:
        return 'INSOMNIA'
    m = 1
    while not check(seen):
        addDigitsToSet(n*m, seen)
        m += 1
    return n*(m-1)
        
inputfile = 'A-large.in'
with open(inputfile, 'r') as f:
    t = f.readline()
    i = 1
    for n in f:
        seen = set()
        result = countSheep(int(n), seen)
        printOutput(i, result)
        i+=1