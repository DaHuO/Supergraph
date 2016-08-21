#!/usr/bin/env python3


# Aralik: 2^(BIT-1)+1 --- 2^BIT-1
# Olusturulan sayi 10'luk tabanda hep tek
# 9. base'den prime olup olmadigina bakilir
# Eger 2. base'e kadar prime degilse bu sayi uygun bir sayidir
# Ardindan asal boleni bulunmaya calisilir


import gmpy2


def coin_jam(bits, m):
    FIRST_NUMBER = 2 ** (bits - 1) + 1
    LAST_NUMBER = 2 ** (bits) - 1

    n = FIRST_NUMBER
    c = 1
    while n < LAST_NUMBER and c <= m:
        l = []
        base = 10
        is_prime = False
        while base >= 2:
            base_n = int(str(gmpy2.digits(n, 2)), base)
            if gmpy2.is_prime(base_n):
                is_prime = True
                break
            l.append(base_n)
            base -= 1
        # Find non trivial divisors
        if not is_prime:
            l.append(gmpy2.digits(n, 2))
            for (i, b) in enumerate(l[:9]):
                divisor = 2
                while divisor < b:
                    if b % divisor == 0:
                        l[i] = divisor
                        break
                    divisor += 1
            print(' '.join(map(str, l[::-1])))
            c += 1
        n += 2

if __name__ == '__main__':
    print('Case #1:')
    coin_jam(16, 50)
