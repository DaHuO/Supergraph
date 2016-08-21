path = "C:/Users/Helge/Downloads/"
file = open(path + 'B-small-attempt0.in', 'r')
output = open(path + 'output', 'w')

numberOfTestcases = file.readline()

def allTrue(pancakes):
    for p in pancakes:
        if not p:
            return False
    return True

def getLastIndexFalse(pancakes):
    i = 0
    last = 0
    for p in pancakes:
        if not p:
            last = i
        i += 1      
    return last

def getFirstIndexFalse(pancakes):
    i = 0
    first = 0
    for p in pancakes:
        if not p:
            return i
        i += 1      
    return i

def flip(pancakes, i):
    return list(map(lambda x: not x, reversed(pancakes[:i])))+pancakes[i:]
        
def solve(pancakes):
    pancakes = pancakes[:getLastIndexFalse(pancakes)+1]
    if allTrue(pancakes):
        return 0    
    if not pancakes[0]:
        return 1 + solve(flip(pancakes, len(pancakes)))
    else:
        return 1 + solve(flip(pancakes, getFirstIndexFalse(pancakes)))
              
    
for testcase_number in range(1, int(numberOfTestcases)+1):
    pancakes = list(map(lambda x: x=='+', file.readline().replace('\n','')))
    solution = 'Case #' + str(testcase_number) + ": " + str(solve(pancakes))
    print(solution)
    output.write(solution + '\n')  
 
output.close()
