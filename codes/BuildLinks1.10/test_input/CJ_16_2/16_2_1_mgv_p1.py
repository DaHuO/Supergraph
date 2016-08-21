num_test = int(raw_input())
for test_case in xrange(1,num_test+1):
    numbers = [0]*10
    strings = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
               "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    code = raw_input()
    cO = 0
    cR = 0
    cV = 0
    cS = 0
    cI = 0
    for c in code:
        if c=='Z':
            numbers[0] += 1
        if c=='O':
            cO += 1
        if c=='W':
            numbers[2] += 1
        if c=='U':
            numbers[4] += 1
        if c=='X':
            numbers[6] += 1
        if c=='G':
            numbers[8] += 1
        if c=='S':
            cS += 1
        if c=='V':
            cV += 1
        if c=='I':
            cI += 1
        if c=='R':
            cR += 1
    
    numbers[1] = cO - numbers[0] - numbers[4] - numbers[2]
    numbers[3] = cR - numbers[4] - numbers[0]
    numbers[7] = cS - numbers[6]
    numbers[5] = cV - numbers[7]
    numbers[9] = cI - numbers[8] - numbers[6] - numbers[5]

    res = ""
    for num in xrange(0, 10):
        for i in xrange(0, numbers[num]):
            res += str(num)
    
    print "Case #{}: {}".format(test_case, res)