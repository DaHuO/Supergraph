import sys;
import random;
from sets import Set


def isPrime(a, primes, l):
    prime = True;
    for p in primes:
        if(p*p > a):
            break;
        if(a%p == 0):
            l.append(p);
            prime = False;
            break;
    return prime;

def getPrimes(primes):
    primes.append(2);

    for i in range(3, 100000, 2):
        if(isPrime(i, primes, [])):
            primes.append(i);

def solve(n, m):
    primes = [];
    getPrimes(primes);
    print "Case #1:";

    found = Set([]);
    while(m):
        temp = random.randrange(0,2**(n-2) - 1);
        s = "1" + format(temp, "0" + str(n - 2) + "b" ) + "1";
        if(s in found):
            continue;
        found.add(s);

        ret = [];
        ok = True;
        for i in range(2, 11):
            if(isPrime(int(s, i), primes, ret)):
                ok = False;
                break;

        if(ok == True):
            print s, " ".join(map(lambda t: str(t), ret));
            m = m - 1;

if __name__ == "__main__":
    data = sys.stdin.readlines();
    n, m = map(lambda num: int(num), data[1].split());

    solve(n, m)
