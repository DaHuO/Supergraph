import logging
import sys

def happy(s):
    return len(s) == sum([1 for x in s if x == '+'])

def flip(s):
    f = {'+':'-', '-':'+'}
    for i,p in enumerate(s):
        if p != s[0]:
            return f[s[0]]*i + s[i:]
    return f[s[0]]*len(s)

def count(s):
    ans = 0
    while not happy(s):
        s = flip(s)
        ans += 1
    return ans

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        S = input()
        print('Case #{}: {}'.format(case + 1, count(S)))
