
from itertools import product
from math import sqrt
from primefac import  *
def fermat(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n - 1, n) == 1


# def get_divisor(num):
#     i = 2
#     while i < sqrt(num):
#         if not num % i:
#             return i
#         i += 1

def get_divisor(n):
    return multifactor(n)



T = int(raw_input())

for case in range(1, T + 1):
    N, J = map(int, raw_input().strip().split())
    j = 0
    print "Case #1:"

    for coin in product('01', repeat=N - 2):
        if j == J: break
        jamcoin = '1' + ''.join(coin) + '1'
        all_base = []


        for n in range(2, 11):
            num = int(jamcoin, n)
            all_base.append(num)
            if fermat(num):
                all_base = []
                break

        else:
            j += 1
            divides = []
            for nu in all_base:
                divides.append(str(get_divisor(nu)))

            print jamcoin, ' '.join(divides)


