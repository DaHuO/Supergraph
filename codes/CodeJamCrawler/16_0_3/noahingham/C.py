import math

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

primes = primes_sieve(10000)

def check(s):
    global primes
    facts=[]
    for b in range(2,11):
        nb = int(s,b)
        good = False
        for prime in primes:
            if(nb%prime==0 and prime<nb):
                facts+=[prime]
                good = True
                # print(s+", "+str(b)+", "+str(nb)+", "+str(prime))
                break
        if not good:
            return False
    print(str(s)+" "+' '.join(map(str,facts)))
    return True

def solve(n,j):
    count=0
    i=0
    while(count<j):
        s = "1"+('{:0'+str(n-2)+'b}').format(i)+"1"
        if(check(s)):
            count+=1
        i+=1
    return ""

if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases+1):
		inp = list(map(int, raw_input().split(" ")))
        print("Case #1:")
        solve(inp[0], inp[1])
