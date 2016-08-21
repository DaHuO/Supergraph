import sys
import math

res = []
J = 0

def translate(binar, base):

    resp = 0;
    multiplier = 1;
    for digit in reversed(binar):
        resp += digit * multiplier
        multiplier = multiplier * base;

    return resp

def is_prime(candidate):

    for divisor in range(2, int(math.sqrt(candidate)) + 2):
        if candidate % divisor == 0:
            return divisor
    return -1

def verify(binar):
    
    global res
    divisors = []
    for base in range(2, 11):
        numb = translate(binar, base)
        divisor = is_prime(numb)
        if divisor != -1:
            divisors = divisors + [divisor]
        else:
            return

    for options in res:
        if binar in options:
            return
    
    divisors = [binar[:]] + divisors[:]
    res = res[:] + [divisors[:]]
        

def permute(binar, index, lb, ub):

    global res
    if len(res) == J:
        return

    verify(binar)

    if index <= lb or index >= ub:
        return

    binar[index] = 1;
    permute(binar, index + 1, lb, ub)

    binar[index] = 0;
    permute(binar, index + 1, lb, ub)
    
    return

#T = sys.stdin.readline()
T = int(raw_input())
cases = 1
while(T):
    res = []
    Jbase = []

    input = sys.stdin.readline()
    N = int(input.split(' ')[0])
    J = int(input.split(' ')[1])

    for i in range(1, N):
        if i == 1:
            Jbase.append(1)
        if i == N - 1:
            Jbase.append(1)
        else:
            Jbase.append(0)
    
    #print is_prime(1111111101100111)
    #exit

    permute(Jbase, 1, 0, N - 1)

    print "Case #" + str(cases) + ":"
    cases = cases + 1
    for num in range (0, J):
        for digit in res[num][0]:
            sys.stdout.write(str(digit))
        sys.stdout.write(' ')
        for index in range(1, len(res[num])):
            sys.stdout.write(str(res[num][index]))
            if(index < len(res[num]) - 1):
                sys.stdout.write(' ')
        sys.stdout.write('\n')
    T = T - 1

