inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())

def get_primes(k):
    is_prime = [1] * (k + 1)
    for num in range(2, k):
        if not is_prime[num]:
            continue
        fact = 2
        while fact * num <= k:
            is_prime[fact * num] = 0
            fact += 1
    primes = []
    for num in range(2, k + 1):
        if is_prime[num]:
            primes.append(num)
    return primes

primes = get_primes(100)            

for test in range(1, t + 1):
    n = int(inf.readline())
    j = int(inf.readline())
    
    print('Case #{}:'.format(test), file = ouf)
    
    left = 2 ** (n - 1)
    right = 2 ** n
    
    done = 0
    
    for num in range(left, right):
        if done >= j:
            print('\nYay!')
            break
        if num % 100 == 0:
            print('Cur = {},    found = {}'.format(num, done))
        if num % 2 == 0:
            continue
        binary = '{0:b}'.format(num)
        
        divisors = [0] * 11
        
        for base in range(2, 11):
            cur = int(binary, base=base)
            for div in primes:
                if cur % div == 0:
                    divisors[base] = div
                    break
        if divisors[2:].count(0) == 0:
            done += 1
            print(binary, *divisors[2:], file = ouf)

inf.close()
ouf.close()