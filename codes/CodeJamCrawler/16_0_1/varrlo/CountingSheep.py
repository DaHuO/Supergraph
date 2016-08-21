def check(digits):
    for i in range(len(digits)):
        if digits[i] == 0:
            return False
    return True

def solve(n):
    digs = [0]*10
    i = 0
    while not check(digs):
        i += 1
        tmp = i*n
        while tmp > 0:
            digs[tmp % 10] = 1
            tmp /= 10
    return i*n


T = int(raw_input())
for t in range(T):
    n = int(raw_input())
    if t != 0:
        print "Case #"+str(t+1)+": "+str(solve(n))
    else:
        print "Case #"+str(t+1)+": INSOMNIA"
   
