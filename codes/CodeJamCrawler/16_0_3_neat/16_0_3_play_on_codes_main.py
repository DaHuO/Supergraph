import random

def factors(coin):
    f = []
    for base in range(2, 11):
        num = int(coin, base)
        # prime test taken from https://en.wikipedia.org/wiki/Primality_test
        prime = False
        if num <= 1:
            continue
        elif num <= 3:
            prime = True
        elif num % 2 == 0:
            f.append(2)
            continue
        elif num % 3 == 0:
            f.append(3)
            continue
        i = 5
        prime = True
        while i*i <= num and i <= 299699:
            # print(i, num)
            if num % i == 0:
                # print('Found factor {} for {} base {} ({})'.format(i, coin, base, num))
                f.append(i)
                prime = False
                break
            elif num % (i + 2) == 0:
                f.append(i + 2)
                prime = False
                break
            i += 6
        if prime:
            return False
    return True, f


t = int(input())
for x in range(1, t + 1):
    n, j = map(int, input().split())
    print('Case #{}:'.format(x))
    k = 1
    for var in range(2**(n - 2)):
        if k > j:
            break
        str_var = bin(var)[2:]
        coin = '1' + '0'*(n - 2 - len(str_var)) + str_var + '1'
        f = factors(coin)
        if f:
            k += 1
            print(coin, *f[1])
