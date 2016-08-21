from itertools import permutations,product
from sys import  *

def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def rangeit(n):
    i = 2
    while i < n:
        yield i
        i += 1

def non_trivial_divisor(n):
    for i in rangeit(int(n**0.5+1)):
        if n % i ==0:
            print 'fact',i
            return i

def is_jam_coin(st):
    for base in xrange(2,11):
        if is_prime(int(st,base)):
            return False
    return True

def permuts(n):
    res = []
    alpha = '01'
    a = n-2
    args = ['1']
    for i in range(a):
        args.append(alpha)
    args.append('1')
    itr = product(*args)
    for i in itr:
        res.append(''.join(i))
    return res


fin = open(argv[1], "r")
fout = open(argv[2],"w")
T = int(fin.readline())


for count in range(T):
    fout.write('Case #' + str(count+1) + ":\n")
    line = fin.readline().strip('\n')
    j,n =int(line.split(' ')[0]),int(line.split(' ')[1])
    print str(j), str(n)
    perms = permuts(j)
    p = 0
    for st in perms:
        if is_jam_coin(st):
            fout.write(st+' ')
            for base in range(2,11):
                e=int(st,base)
                print 'e: ',
                print e
                fout.write(str(non_trivial_divisor(e))+' ')
            fout.write('\n')
            p += 1
        print p
        if p == n:
            break
print 'done'

fin.close()
fout.close()