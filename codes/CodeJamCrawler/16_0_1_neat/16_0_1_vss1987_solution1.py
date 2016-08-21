'''
solution for counting sheep
'''

def getDigits(n):
    digits = []
    while n>0:
        digits.append(n%10)
        n = n//10
    return digits

def isSolution(allDigits):
    res = True
    for digit in allDigits:
        res = res and digit

    return res

def solve(n):
    allDigits = [False]*10
    count = 1
    while True:
        if n == 0:
            return 'INSOMNIA'
        number = n*count
        digits = getDigits(number)

        for d in digits:
            allDigits[d] = True

        if isSolution(allDigits):
            return number
        count += 1


file = 'A-large'
inp = open(file+'.in', 'r').read().splitlines()
out = open(file+'.out', 'w')
case = 0
testcases = int(inp[0])
case = 0
for tc in range(1, testcases+1, 1):
    res = solve(int(inp[tc]))
    case += 1
    out.write('Case #' + str(case) + ': ' + str(res) + '\n')