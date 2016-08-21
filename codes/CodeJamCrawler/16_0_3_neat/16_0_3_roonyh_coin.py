import math

N = 16
J = 50

def is_prime(n):
    if n == 2:
        return True, 0
    if n % 2 == 0 or n <= 1:
        return False, 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False, divisor
    return True, 0

max = int("".join(['1']*(N-2)), 2)

print 'Case #1:'

jamCoinCount = 0;

for mid in range(max+1):
    n = "1{0:014b}1".format(mid)
    isJamCoin = True;
    divisors = [];
    for base in range(2, 11):
        num = 0
        b = 1
        for i in n[::-1]:
            if(i == '1'):
                num = num + b
            b = b*base
        isp, div = is_prime(num)
        if(isp):
            isJamCoin = False
            break
        else:
            divisors.append(div)

    if(isJamCoin):
        jamCoinCount = jamCoinCount+1
        print n, ' '.join(str(x) for x in divisors)

    if(jamCoinCount == J):
        break