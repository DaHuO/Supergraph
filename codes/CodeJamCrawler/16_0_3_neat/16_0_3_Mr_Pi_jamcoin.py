import sys
import math

sieve = set([2,3])

def isprime(val, addp=False):
    if val % 2 == 0: return 2
    for i in sieve:
        if val % i == 0:
            return i
    nextstart = (1 + max(sieve)/6) * 6 - 1
    nextend = int(math.sqrt(val))+1
    if not addp: nextend = min(nextend, 5000)
    #nextend = int(math.sqrt(val))+1
    #nextstart = max(sieve)+2
    #for i in xrange(nextstart, int(math.sqrt(val))+1, 2):
    for i in xrange(nextstart, nextend, 6):
        if isprime(i, addp=True) == -1:
            if val % i == 0:
                return i
        if isprime(i+2, addp=True) == -1:
            if val % (i+2) == 0:
                return i+2
    if addp: sieve.add(val)
    return -1
            
        

if __name__ == "__main__":
    f = open(sys.argv[1])
    T = int(f.readline().strip())
    for i in xrange(1,T+1):
        N,J = map(int, f.readline().strip().split())
        print("Case #"+str(i)+":")
        startval = int("1"+"0"*(N-2)+"1", 2)
        K = 0
        while K < J:
            startstr = bin(startval)[2:]
            ans = []
            for n in xrange(2,10+1):
                val = int(startstr, n)
                factor = isprime(val)
                if factor == -1:
                    break
                ans.append(factor)
            if len(ans) == 9:
                print(startstr+" "+" ".join(map(str, ans)))
                K += 1
            startval += 2
            #sys.stderr.write(str(startstr)+" "+str(K)+" "+str(len(sieve))+"\n")
            #sys.stderr.flush()
    f.close()
