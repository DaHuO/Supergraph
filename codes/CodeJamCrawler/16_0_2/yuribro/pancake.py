import sys
import os

cache = {}

def prepare(s):
    return s.strip()

def flip(s):
    other = {'-': '+',
             '+': '-'}
    
    return ''.join([other[x] for x in s][::-1])

def solve(s):
    if s not in cache:
        if '-' not in s:
            return 0

        if '+' == s[-1]:
            return solve(s[:-1])
        else:
            cache[s] = 9999999
            cache[s] = solve(flip(s)) + 1
            
            for i in xrange(1, len(s)):
                cache[s] = min(cache[s], solve(flip(s[:-i]) + s[-i:]) + 1)

    return cache[s]
    

def read_input():
    with open(sys.argv[1]) as input_file:
        T = int(input_file.readline())
        for i in xrange(T):
            S = input_file.readline()
            S = prepare(S)
            answer = solve(S)
            print 'Case #{}: {}'.format(i+1, answer)

            
if __name__ == "__main__":
    read_input()
