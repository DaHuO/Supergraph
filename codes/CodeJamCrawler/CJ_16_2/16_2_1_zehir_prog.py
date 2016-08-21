#! /usr/bin/env python3

digits = { 0 : 'ZERO',
          1 : 'ONE',
          2 : 'TWO',
          3 : 'THREE',
          4 : 'FOUR',
          5 : 'FIVE',
          6 : 'SIX',
          7 : 'SEVEN',
          8 : 'EIGHT',
          9 : 'NINE'
         }

def gen_nums(n):
    if n == 1:
        return [[x] for x in list(range(10))]
    l = gen_nums(n - 1)
    res = []
    for num in l:
        if n > 1:
            for i in range(num[-1], 10):
                res.append(num + [i])
    return res

def gen_spelling(num):
    res = ''
    for i in num:
        res += digits[i]
    return res

def g(n, s):
    s = sorted(s)
    nums = gen_nums(n)
    for num in nums:
        if (sorted(gen_spelling(num)) == s):
            return num
    return []

def f(s):
    for n in range(1, 3 * len(s)):
        l = g(n, s)
        if l != []:
            return ''.join([str(x) for x in l])
    return []

t = int(input())
for i in range(1, t + 1):
    s = input()
    print('Case #{}: {}'.format(i, f(s)))
