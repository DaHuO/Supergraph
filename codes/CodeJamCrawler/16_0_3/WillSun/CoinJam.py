import math

def bin2other(radix, bin = ""):
    num = 0
    count = 1
    bin_len = len(bin)
    while bin_len - count >= 0:
        num = num + int(bin[bin_len - count]) * (radix**(count - 1))
        count = count + 1
    return num

def isPrime(num):
    #only find 2 to 50 divisor
    for i in range(2, 50):
        if num % i == 0:
            return i
    return 0

t = int(input())
print("Case #{}: ".format(t))
for i in range(1, t + 1):
    n, j = [int(s) for s in input().split(" ")]
    count = 0
    for num in range(2**(n - 1) + 1, 2**n, 2):
        if count >= j:
            break
        is_prime = 0
        divisors = []
        for i in range(2, 11):
            divisor = isPrime(bin2other(i, bin(num)[2:]))
            if divisor == 0:
                is_prime = 1
                break
            divisors.append(divisor)
        if is_prime == 1:
            continue
        print(bin(num)[2:], end = ' ')
        print(' '.join(str(x) for x in divisors))
        count = count + 1