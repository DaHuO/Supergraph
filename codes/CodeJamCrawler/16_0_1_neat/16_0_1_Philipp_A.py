def solveA():
    T = int(input())
    c = 0
    while c < T:
        c += 1
        N = int(input())
        result = "Case #%i: %s" % (c, solve(N))
        print(result)
def solve(N):
    if N == 0:
        return 'INSOMNIA'
    
    bools = [False] * 10
    
    current = N
    while True:
        for c in str(current):
            bools[int(c)] = True
        if allTrue(bools):
            return str(current)
        current += N

            
def allTrue(bools):
    for b in bools:
        if not b:
            return False
    return True
solveA()