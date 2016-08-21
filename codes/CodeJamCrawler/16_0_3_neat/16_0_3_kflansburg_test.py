

N = 16

import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def factor(n):
    c = 2
    while n%c!=0:
        c+=1
    return c

def increment(n):
    return ("{:0%db}"%(N-2)).format(1 + int(n, 2))

import time
t = time.time()
J = 50
core = (N-2)*"0"
L = []
found = 1
while len(L)<J:
    s = "1"+core+"1"
    l = map(lambda n: int(s,n), list(range(2,11)))
    check = all(map(lambda n: not is_prime(n),l))
    if check:
        print "FOUND: %d/%d"%(found,J)
        found+=1
        f = map(lambda n: factor(n),l)
        L.append((s,f))
    core = increment(core)
print time.time()-t
f = open('output.txt','w')
f.write("Case #1:\n")
for l in L:
    f.write(l[0]+" ")
    f.write(" ".join(map(lambda n: str(n),l[1]))+"\n")

f.close()
