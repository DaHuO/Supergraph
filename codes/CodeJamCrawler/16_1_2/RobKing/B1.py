from numpy import * 

def solve(T, N):
    boollist = {}
    for i in range(2 * N - 1):
        input = raw_input().split()
        input = map(int, input)
        for number in input:
            if number in boollist:
                boollist[number] = not boollist[number]
            else:
                boollist[number] = True
    result = []
    for key in boollist.keys():
        if boollist[key]:
            result.append(key)
    result.sort()
    resultstr = ' '.join(map(str, result))
    print "Case #%d: %s" %(T+1, resultstr)


cases = int(raw_input())
for T in xrange(cases):
    N = int(raw_input())
    solve(T, N)
