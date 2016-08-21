import sys

def solve(n):
    if n<=0: return 'INSOMNIA'
    digits = set([str(num) for num in range(10)])
    num = 0
    while len(digits)>0:
        num+=n
        for ch in str(num):
            if ch in digits:
                digits.remove(ch)
    return num
    print(digits)

with open(sys.argv[1],'r') as f:
    testcases = int(f.readline())
    for t in range(1,testcases+1):
        line = f.readline()[:-1]
        print('Case #%d: %s' % (t,solve(int(line))))
