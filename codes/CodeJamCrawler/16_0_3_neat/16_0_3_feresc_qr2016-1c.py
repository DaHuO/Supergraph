#!python

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def isCoinjam(s, primes):
    for b in range(2,11):
        if int(s,b) in primes:
            return False
    return True

def getDivisor(n, primes):
    for x in primes:
        if n%x == 0:
            return x
    
def solve(n,j, primes):
    for x in xrange(n/2+1,n,2):
        bcode = bin(x)[2:]
        if isCoinjam(bcode, primes):
            print bcode,
            for b in range(2,11):
                print getDivisor(int(bcode,b), primes),
            print
            j -= 1
            if j == 0:
                break
        

def main():
    primes = sieve_for_primes_to(2**27)
    n = int(raw_input())
    for c in range(1, n + 1):
        n, j = map(int, raw_input().split())
        print 'Case #1:'
        solve(2**n,j, primes)

if __name__ == "__main__":
  main()
    
