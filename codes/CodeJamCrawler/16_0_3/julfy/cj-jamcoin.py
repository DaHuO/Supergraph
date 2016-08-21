import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0

def get_next (n,l):
    return bin(n)[2:].zfill(l-2),n+1

def interpret(n,b):
    sum = 0
    mul = 1
    for c in reversed(n):
        if c == '1':
            sum += mul
        mul *= b
    return sum

def get_tokens(jam):
    tokens = []
    for base in range(2,11):
        n = interpret(jam,base)
        token = is_prime(n)
        if token == 0:
            return []
        else:
            tokens.append(str(token))
    return tokens

def get_jams(l,n):
    i = 0
    cur = 0
    while i < n:
        sub,cur = get_next(cur,l)
        jam = '1'+sub+'1'
        tokens = get_tokens(jam)
        if tokens == []:
            continue;
        else:
            print jam," ".join(tokens)
        i +=1


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n,m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}:".format(i)
    get_jams(n,m)
    # check out .format's specification for more formatting options
