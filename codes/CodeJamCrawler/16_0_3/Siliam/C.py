if __name__ == "__main__":
    testcases = input()

    def eval_in_base(jam, base):
        coef = 1
        val = 0
        for c in jam[::-1] :
            val += int(c) * coef
            coef *= base
        return val
    
    def write_in_base(num, base):
        val = 0
        coef = 1
        while num > 0:
            val += (num % base)*coef
            coef *= 10
            num /= base
        return val
    
    # Sieve of Eratosthenes
    def primes_upto(limit):
        is_prime = [False] * 2 + [True] * (limit - 1) 
        for n in range(int(limit**0.5 + 1.5)):
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    def factor(n, primes):
        for p in primes :
            if n % p == 0 and n != p :
                return p
        return 1
        
    for caseNr in xrange(1, testcases+1):
        N, J = map(int, raw_input().split())
        limit = 10**(N/2)
        p = primes_upto(limit)
        
        counter = 0 
        print "Case #" + str(caseNr) + ":" 
        
        for x in xrange(2**(N - 2)):
            core = str(write_in_base(x, 2))
            core = "0"*(N - 2 - len(core)) + core
            jam = "1" + core + "1"
            
            factors = []
            for i in range(2, 11):
                n = eval_in_base(jam, i)
                f = factor(n, p)
                if f == 1: # not prime
                    break
                factors.append(f)
            
            if len(factors) < 9 : continue #not a prime in all bases
            else : counter += 1
            
            print jam + " " + " ".join(map(str, factors))
            
            if counter == J:
                break