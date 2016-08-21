def countSheep(N):
    if N == 0:
        return "INSOMNIA"
    factor = 1
    digits = set(list(str(N)))
    retVal = N
    complete = list("0123456789")
    while 1:
        if sorted(digits) == complete:
            return str(retVal)
        factor += 1
        retVal += N
        digits = digits.union(set(list(str(retVal))))

T = int(input())
for i in range(1,T+1):
    print("Case #%d: %s" % (i, countSheep(int(input()))))
