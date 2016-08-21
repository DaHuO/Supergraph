#!/usr/bin/env python3

def get_factor(n):
    if n % 2 == 0: return 2
    for f in range(3, int(n**0.5)+2, 2):
        if n % f == 0: return f

def get_answer(n):
    ans = [n]
    for base in range(2, 11):
        k = int(str(n), base)
        f = get_factor(k)
        if f is None:
            return None
        ans.append(f)
    return ans

assert input() == '1'
print('Case #1:')
N, J = map(int, input().split())
first = 10**(N-1)+1
last = int('1' * N)
cnt = 0
while first < last and cnt < J:
    ans = get_answer(first)
    if ans is not None:
        print(' '.join(map(str, ans)))
        cnt += 1
    first = int(bin(int(str(first), 2) + 2)[2:])
