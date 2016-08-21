path = "C:/Users/Helge/Downloads/"
file = open(path + 'A-small-attempt0.in', 'r')
output = open(path + 'output', 'w')

numberOfTestcases = file.readline()

def getDigistIn(N):
    digits = set()
    while N > 0:
        digits.add(N%10)
        N = N//10
    return digits
    
def solve(N):
    digits = set()
    i = 1
    while len(digits) < 10:
        digits.update(getDigistIn(i*N))
        i += 1
        if i > 10000:
            return 'INSOMNIA'
    return str((i-1)*N)

for testcase_number in range(1, int(numberOfTestcases)+1):
    N = int(file.readline())
    solution = 'Case #' + str(testcase_number) + ": " + solve(N)
    print(solution)
    output.write(solution + '\n')  
 
