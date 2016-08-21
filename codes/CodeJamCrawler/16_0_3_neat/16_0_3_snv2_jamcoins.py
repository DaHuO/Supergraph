__author__ = 'snv'
from random import randint
UPPER_LIMIT = 2000000    # до какого числа ищем простые

def get_primes(n):
    """  Создание списка простых чисел меньших n
    :param n: верхняя границаб до которой ищем простые числа
    :return: отсортированный список простых чисе от 2 до n
    """
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    primes_list = list(primes)
    primes_list.sort()
    return primes_list

primes = get_primes(UPPER_LIMIT)


N=32
J=500
MAXDIV= 10**(5)

coins = []

print('Case #1:')
for j in range(J):
    bad = True
    while bad:
        bad = False
        coin = '1'+''.join(str(randint(0,1)) for n in range(N-2))+'1'
        if coin in coins:
            continue

        divs = []
        for k in range(2,11):
            num = int(coin, base=k)
            if num in primes:
                bad = True
                continue
            for div in range(2,MAXDIV):
                if num % div == 0:
                    tmp = num //div
                    if tmp * div == num:
                        divs.append(div)
                        break
        bad = (len(divs) < 9)
    coins.append(coin)
    print(coin, " ".join(str(d) for d in divs))

