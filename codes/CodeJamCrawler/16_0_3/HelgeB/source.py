path = "C:/Users/Helge/Downloads/"
output = open(path + 'output', 'w')

solution = 'Case #1:'
print(solution)
output.write(solution + '\n')  

N = 32
J = 500

n = pow(2, N-1)+1


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

primes = primes_sieve(pow(10, 7))

def getDiv(num):
    for p in primes:
        if num%p == 0:
            return p
        if p*p > num:
            return None

def isPrime(num):
    return num in primes

def toBin(n):
    return bin(n)[2:]

def interpretBase(binary, base):
    b = reversed(binary)
    result = 0
    i = 0
    for c in b:
        if c == '1':
            result += pow(base,i)
        i += 1
    return result
    
def jam(n):
    binary = toBin(n)
    result = str(binary)
    for base in range(2,11):
        div = getDiv(interpretBase(binary, base))
        if div == None:
            return ""
        result = result + " " + str(div)
    return result



while J > 0:
    j = jam(n)
    if len(j) > 0:
        J -= 1
        print(j)
        output.write(j + '\n')   
    n += 2

output.close()