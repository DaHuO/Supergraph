import itertools
from itertools import repeat
def dup_perms(seq, rep=0):
    for p in itertools.product(seq, repeat=rep):
        yield ''.join(p)
        
def isprime(n):
    if n == 1:
        return False
    for i in xrange(2, n):
        if n % i == 0:
            return False
    return True

def divider(n):
    if n % 2 == 0 and n != 2:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0 and n != i:
            return i
        i += 2
    return -1

def solve(N, J):
    ret = ''
    gen1 = dup_perms('01', rep=((N-2)/2))
    gen2 = dup_perms('01', rep=((N-2)/2)+((N-2)%2))
    while J > 0:
        v = '1' + gen1.next() + gen2.next() + '1'
        j = [divider(int(v, base=i)) for i in range(2,11)]
        if all(n != -1 for n in j):
            s = v + ' ' + ' '.join(map(str, j)) + '\n'
            ret += s
            J -= 1
    return ret

if __name__ == '__main__':
    case_num = int(raw_input())
    for i in range(1, case_num+1):
        N, J = map(int, raw_input().split())
        print 'Case #%d:\n%s' % (i, solve(N, J))