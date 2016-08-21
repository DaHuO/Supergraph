
prime_test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def pow(a, d, n):
    m = a
    r = m if d & 1 == 1 else 1
    d >>= 1
    while d > 0:
        m = (m * m) % n
        if d & 1 == 1:
            r = (r * m) % n
        d >>= 1
    return r
# assert pow(2, 10, 1111) == 1024
# assert pow(23, 7, 245) == 177

def is_prime(a, n):
    if n == 1 or n & 1 == 0:
        return False
    elif n == 2:
        return True
    else:
        d = n-1
        while d & 1 == 0:
            d >>= 1
        t = pow(a, d, n)
        while (d != n-1) and (t != 1) and (t != n-1):
            t = (t * t) % n
            d <<= 1
        return t == n-1 or d & 1 == 1
# assert is_prime(2, 3)
# assert not is_prime(2, 341)

# def search_factor(n):
#     if n & 1 == 0:
#         return 2
#     elif str(n)[-1] == '5':
#         return 5

#     from math import sqrt
#     factor = int(sqrt(n))
#     while factor >= 2:
#         if n % factor == 0:
#             break
#         else:
#             factor -= 1
#     return factor

def pollard(n):
    if n & 1 == 0:
        return 2
    elif str(n)[-1] == '5':
        return 5

    from random import randrange
    from fractions import gcd
    x = randrange(2,1000000)
    c = randrange(2,1000000)
    y = x
    d = 1
    while d == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        d = gcd(x-y, n)
        if d == n:
            break
    return d

def in_base(n, m):
    acc = 0
    nums = enumerate(reversed(list(map(lambda x: int(x), n))))
    for i, x in nums:
        if x == 1:
            acc += m ** i
    return acc

def solve(n):
    global prime_test
    n_str = '{0:b}'.format(n)
    nums = []
    for i in range(2, 11):
        num = in_base(n_str, i)
        if all(map(lambda x: is_prime(x, num), prime_test)):
            return None, None
        nums.append(num)
    # print(nums)

    results = [pollard(num) for num in nums]
    # print(results)
    
    return n_str, ' '.join(list(map(lambda x: str(x), results)))


t = int(input())
for i in range(1, t+1):
    n, m = [int(s) for s in input().split(' ')]
    
    print('Case #{}:'.format(i))
    num = 2 ** (n-1) + 1
    while num <= 2 ** n - 1:
    # num = 2 ** n - 1
    # while num >= 2 ** (n-1) + 1:
        binary, result = solve(num)
        if result:
            print('{} {}'.format(binary, result))
            m -= 1
            if m == 0:
                break
        
        num += 2
