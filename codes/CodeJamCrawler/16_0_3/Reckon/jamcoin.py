from math import sqrt
# Should always be availble with Python 2.7

def read_base(base, n):
    l = zip(range(0, len(n)), map(lambda x : int(x), n)[::-1])
    f = lambda x, y: y[1]*(base**(y[0])) + x
    return reduce(f, l, 0)

def check_prime(n):
    div = 2
    
    while div <= sqrt(n):
        if (n % div) == 0:
            return div
        div += 1
    return None

def to_binary(n, length):
    printed_one = False

    s = ""
    while n >= 2:
        rem = n % 2
        s += str(rem)
        n = (n - rem) / 2
    s += str(n)
    s = s[::-1]
    while len(s) < length:
        s = '0' + s
    return s
    
count = int(raw_input())
line = raw_input().split()

for i in range(0, count):
    N = int(line[0])
    J = int(line[1])

    c = 0
    print "Case #" + str(i+1) + ":"

    for k in range(32769, 65536):
        if k % 2 == 0:
            continue

        s = to_binary(k, N)

        
        all_divisors = []

        for base in range(2, 11):
            n = read_base(base, s)
            divisor = check_prime(n)

            if divisor == None:
                all_divisors = []
                break
            all_divisors.append(divisor)
       # If divisors were found in all bases    
        if len(all_divisors) > 0:
            print s,
            for div in all_divisors:
                print div,
            print
            c += 1
            if c >= J:
                break
            
#    for k in range(0, 2**(N-2)):
#        s = ''
#        if N-2 > 0:
#            s = '1' + to_binary(k, N-2) + '1'
#        else:
#            s = '11'
#        all_divisors = []

#        print s
        
        # For each base 2 - 10
#        for base in range(2, 11):
#            n = read_base(base, s)
#            divisor = check_prime(n)
            
#            if divisor == None:
#                all_divisors = []
#                break
#            all_divisors.append(divisor)
        # If divisors were found in all bases    
#        if len(all_divisors) > 0:
#            print s,
#            for div in all_divisors:
#                print div,
#            print
#            c += 1
#            if c >= J:
#                break
