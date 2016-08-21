def calculate(n):
    seen = [False,False,False,False,False,False,False,False,False,False]
    count = 0
    for i in xrange(1, 101):
        digits = str(n*i)
        for digit in digits:
            j = int(digit)
            if seen[j]==False:
                seen[j] = True
                count = count + 1
            if count == 10:
                return int(digits)
    return "INSOMNIA"
    
t = int(raw_input())       
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, calculate(n))