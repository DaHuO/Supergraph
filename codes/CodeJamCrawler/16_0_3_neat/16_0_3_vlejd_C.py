from itertools import product

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

P = primes(1000000)

def num (n, base):
    nn = 0
    for x in n:
        nn = nn*base + x
    return nn
    
def check (n, base):
    nn=num(n,base)
    d = 1
    for p in P:
        if p*p>=nn: break
        
        if not nn%p:
            d=p
            break
    return d
    
    

def solve(t):
    print "Case #%d:"%(t+1)
    N, J = map(int, raw_input().strip().split())
    fine = []
    for p in product(range(2), repeat= N-2):
        if len(fine)>= J: break
        pp = (1,)+p + (1,)
        divs = []
        for b in xrange(2,11):
            d = check(pp, b)
            if d==1:
                break
            divs.append((d))
        if len(divs)==9:
            fine.append((pp, divs))
                
    for r in fine[:J]:
        print ''.join(map(str,r[0])), ' '.join(map(str,r[1]))
    pass

def main():
    T = input()
    for i in xrange(T):
        solve(i)
    
if __name__=="__main__":
    main()