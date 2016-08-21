import math

base = [2,3,4,5,6,7,8,9,10]

def is_prime_c(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, 100 + 1, 2):
        if n % i == 0:
            return False
    return True



def check_prime_through_bases(x):
 for b in base:
     if is_prime_c(int(str(x),b)):
         return False
 return True


def divisorGenerator_c(n):
    large_divisors = []
    for i in xrange(1, 100):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def get_nontrivialdivisor(x):
    a = list(divisorGenerator_c(x))
    a.remove(1)
    a.remove(x)
    return a[0]
    
def get_list_nontrivialdivisor(x):
    res = ''
    for b in base:
        res = res + str(get_nontrivialdivisor(int(str(x),b))) + ' '
        
    return res

 
x = '10000000000000000000000000000001'
add = '10'
J = 1

while(J<501):
 if check_prime_through_bases(x):
    
    print x, get_list_nontrivialdivisor(x)
    J=J+1
 x = bin(int(x,2) + int(add,2))[2:]
 
        