
# coding: utf-8

# In[13]:

import itertools
import random


# In[37]:

def divisors(n):
    original = n
    div = 2
    while div**2 <= n:
        while n % div == 0:
            yield div
            n //= div
        div += 1
    if n > 1 and n < original:
        yield n


# In[38]:

def some_divisor(n):
    for divisor in divisors(n):
        return divisor
    return False


# In[39]:

def check_coin(coin):
    divs = []
    for base in range(2, 11):
        n = int(coin, base)
        div = some_divisor(n)
        if not div:
            return False
        divs.append(div)
    return divs


# In[69]:

def solve(j, n):
    high = 2 ** (j-2)
    seen = set()
    for i in range(n):
        divisors = False
        while not divisors:
            coin = bin(high + random.randrange(high))[2:] + "1"
            if coin in seen:
                continue
            seen.add(coin)
            divisors = check_coin(coin)
            if not divisors:
                continue
            print("{} {}".format(coin, " ".join(map(str, divisors))))


# In[71]:

cases = int(input())
for case in range(1, cases+1):
    j, n = map(int, input().split(" "))
    print("Case #{}:".format(case))
    solve(j, n)

