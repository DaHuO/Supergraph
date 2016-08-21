def makeTruthTable(sourceInt):
    return [True if str(x) in str(sourceInt) else False for x in range(10)]

T = int(input())
for i in range(T):
    N = int(input())
    tmpN = N
    truthTable = makeTruthTable(tmpN)

    if N == 0: 
        print("Case #%i: INSOMNIA" % (i+1))
        continue

    while(sum(truthTable) != 10):
        tmpN += N
        truthTable = list(map(any, zip(*[truthTable, makeTruthTable(tmpN)])))

    print("Case #%i: %i" % (i+1, tmpN))
    continue