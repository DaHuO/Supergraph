from math import sqrt

def is_prime(n):
    if n<=1:
        return False, 1;
    if n==2:
        return True, -1;
    if n%2==0:
        return False, 2;
    m=sqrt(n);

    i=3
    while i<=m:
        if (n%i==0):
            return False, i;
        i+=2
    return True, -1;

def is_jam_coin(n):
    base = 2
    ret = []
    while base <= 10:
        bn = int(n,base)
        isprime, factor = is_prime(bn)
        if isprime:
            return False
        else:
            # print n, base, bn, factor
            ret.append(factor)
        # else:
        #     print ":", bn
        base += 1
    return ret

T = input()
NJ = raw_input().split(' ')
N = int(NJ[0])
J = int(NJ[1])
i=0

answers = 0
print "Case #1:"
while True:
    b = bin(i)[2:]
    bz = b.zfill(N-2)
    c = '1' + bz + '1'
    # print "* ", c
    result = is_jam_coin(c)
    if result:
        # print c, 
        answers += 1
        ret = [c] + result
        print ' '.join(map(str,ret))
    if answers == J:
        break
    i += 1
