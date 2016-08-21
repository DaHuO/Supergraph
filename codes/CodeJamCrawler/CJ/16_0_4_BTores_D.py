def solve( case ):
    caseArray = case.split()
    k, c, s = (int(x) for x in caseArray)

    if(k == 1):
        return 1
    return  ' '.join([str(k) for k in range(1, k+1)])
    
caseNumbers = input()
for caseN in xrange(1, caseNumbers+1):
    case = raw_input()
    print("Case #%i: %s" % (caseN, solve(case)))
