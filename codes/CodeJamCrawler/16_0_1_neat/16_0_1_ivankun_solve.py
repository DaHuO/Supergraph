#!/usr/bin/python3

def read(): return tuple(map(int, input().split()))

def solve():
    n = input()
    s = set(n)
    sn = int(n)
    for i in range(1000):
        if len(s) == 10:
            return n
        n = str((i + 2) * sn)
        s.update(set(n))
    return 'INSOMNIA'

if __name__ == '__main__':
    for _ in range(int(input())):
        print('Case #%i: %s' % (_ + 1, solve()))
