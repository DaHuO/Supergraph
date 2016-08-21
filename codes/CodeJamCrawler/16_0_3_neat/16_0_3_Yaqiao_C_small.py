
def is_prime(n):
    """
    determine whether n is a prime or not
    """
    """Returns True if n is prime. This method is 10 times more efficient"""
    if n == 2:
        return True, None
    if n == 3:
        return True, None
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return (False, i)
        i += w
        w = 6 - w  # based on the fact that a prime is only in the form of 6k-1 or 6k+1
    return True, None

def func(N,J, is_prime_set = True):
    """
    S: a string contains '+' and '-'
    return the last number before sleep, if never stop, return INSOMNIA
    dont try to change S
    """

    
    
    res = []
    MIN = int('0'*(N-2),2)
    MAX = int('1'*(N-2),2)
    
    
    M1 = long('1' + '0'*(N-2) + '1', 2)
    M2 = long('1' + '1'*(N-2) + '1', 10)
    M2 = min(M1 * 100, 1e11)
    print 'M2', M2
    prime_set = set() # store all the primes from M1 to M2, since prime number is sparse, time complexity is OK
    
    if is_prime_set:
        n =  M1
        while n <= M2:
            #print n
            tmp = is_prime(n)
            if tmp[0]:
                prime_set.add(n)
                print n
            n += 2
            
    for n in range(MIN,MAX + 1):
        tmp = bin(n)[2:]
        tmp = '0' * (N-2 - len(tmp)) + tmp
        tmp = '1' + tmp + '1'
        # calculate the real val of different base
        flag = 0
        divisors = []
        for base in range(2,11):
            val = int(tmp, base)
            # determine whether val is a prime or not
            if val in prime_set:
                flag = 1
                break
            else:
                res_prime = is_prime(val)
                if res_prime[0]: # in case the val is too large
                    flag = 1
                    break
                divisors.append(res_prime[1])

        # is always a non-prime
        if flag == 0: 
            print tmp
            res.append([tmp,divisors])
            
        if len(res) == J:
            return res
    return res
        

import time
t1 = time.time()
res = func(16,50, is_prime_set = False)
t2 = time.time()
print res
print 'time elapsed', t2-t1
file_name = 'result_C_small.txt'
with open(file_name,'w') as f:
        res_str = 'Case #1:\n'
        for tmp in res:
            res_str += tmp[0] + ' ' + ' '.join([str(div) for div in tmp[1]]) + '\n'
        f.write(res_str)

    
    
