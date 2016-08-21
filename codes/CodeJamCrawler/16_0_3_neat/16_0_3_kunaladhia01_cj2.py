#n = length
#j = number
def isprime(n):
    #n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True
    #if not n & 1:
    if n % 2 == 0:
        return 2
    for x in range(3, 501, 2):
        if n % x == 0:
            return x
    return -1
def increment(count, length):
    for i in range(length-1, -1, -1):
        if count[i] == 0:
            count[i] = 1
            return count
        else:
            count[i] = 0
    return count
times = int(input())
for d in range(times):
    ud = input()
    n = int(ud[:ud.index(' ')])
    j = int(ud[ud.index(' ') + 1:])
    bit = [0 for c in range(n)]
    bit[0] = 1
    bit[n-1] = 1
    count = 0
    print("Case #1:")
    while count < j:
        num = ''
        for i in range(n):
            num += str(bit[i])
        vals = []
        for i in range(9):
            vals.append(int(num, i+2))
        e_f = False
        factors = []
        #print(vals)
        for e in vals:
            if isprime(e) == -1:
                e_f = True
                break
            else:
                factors.append(isprime(e))
        for i in range(2):
            bit = increment(bit, n)
        if e_f:
            continue
        count+=1
        top = str(vals[8]) + ' '
        for i in range(8):
            top += str(factors[i]) + ' '
        top += str(factors[8])
        print(top)
        
                
    
