#!/usr/bin/env python3

def expand_chars(c):
    if c == 'R':
        return 'RS'
    elif c == 'P':
        return 'PR'
    elif c == 'S':
        return 'PS'

class Node:
    def __init__(self, val):
        self.val = val

    def expand(self):
        if self.val:
            self.children = list(map(Node, expand_chars(self.val)))
            self.val = None
        else:
            for c in self.children:
                c.expand()
        return self

    def sort(self):
        if not self.val:
            self.val = ''.join(sorted(c.sort() for c in self.children))
        return self.val


def compute_rps_tree(n, R, P, S):
    if n == 0:
        return Node('R'*R + 'P'*P + 'S'*S)
    a, b, c = sorted([R, P, S])
    if a + b < c:
        return None
    left = R+P-S
    rp = left // 2
    rs = R - rp
    sp = P - rp
    res = compute_rps_tree(n-1, rs, rp, sp)
    return res and res.expand()

def compute_rps(n, R, P, S):
    res = compute_rps_tree(n, R, P, S)
    if res == None:
        return 'IMPOSSIBLE'
    return res.sort()

def run_test(i):
    nums = map(int, input().split())
    print('Case #%d: %s' % (i, compute_rps(*nums)))

def main():
    T = int(input())

    for t in range(T):
        run_test(t+1)

def extensive():
    import random
    for i in range(100000):
        compute_insomnia(random.randint(0, 10**6))
    exit(0)

if __name__ == '__main__': main()