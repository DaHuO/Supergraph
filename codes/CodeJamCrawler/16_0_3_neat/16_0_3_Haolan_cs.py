def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return 0
    # 2 is the only even prime number
    if n == 2: 
        return 0
    # all other even numbers are not primes
    if not n & 1: 
        return 2
    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return x
    return 0

def trans(digits,base):
    size = len(digits)
    s = sum(digits[i]*(base**i) for i in range(size))
    return s

def next(digs):
    size = len(digs)
    carry = 0
    for i in range(1,size-1):
        if digs[i] == 0:
            digs[i] = 1
            return
        else:
            digs[i] = 0

times = 1#int(input())
for t in range(times):
    print 'Case #'+str(t+1)+':'
    (N,J) = (16,50)#[int(a) for a in raw_input().split(' ')]
    j = 0
    digits = [1]+[0 for i in range(N-2)]+[1]
    while j < J:
        ls = []
        success = True
        for base in range(2,11):
            a = isprime(trans(digits,base))
            if a == 0:
                success = False
                break
            else:
                ls.append(a)
        if success:
            digits.reverse()
            digstr = ''.join([str(a) for a in digits])
            print digstr+' '+' '.join([str(a) for a in ls])
            j += 1
        next(digits)

