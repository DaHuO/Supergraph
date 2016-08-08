#!/usr/bin/env python3

#from itertools import permutations

# def verify(perm):
#     #print("VERIFY " + (''.join(perm)))
#     if len(perm) <= 1:
#         return True
#     next = []
#     i = 0
#     while i < len(perm):
#         a, b = perm[i], perm[i+1]
#         if a == b:
#             return False
#         if (a == 'P' and b == 'R') or (a == 'R' and b == 'P'):
#             next.append('P')
#         elif (a == 'P' and b == 'S') or (a == 'S' and b == 'P'):
#             next.append('S')
#         elif (a == 'S' and b == 'R') or (a == 'R' and b == 'S'):
#             next.append('R')
#         i += 2
#     return verify(next)

def layer(r, p, s, last):
    if r + p + s == 1:
        if r:
            return 'R'
        if p:
            return 'P'
        if s:
            return 'S'

    nr, np, ns = 0, 0, 0
    while (r or p or s):
        if r > p and s > p:
            r -= 1
            s -= 1
            #pairs.append("RS")
            nr += 1
            continue
        if p > r and s > r:
            p -= 1
            s -= 1
            #pairs.append("PS")
            ns += 1
            continue
        if p > s and r > s:
            p -= 1
            r -= 1
            #pairs.append("PR")
            np += 1
            continue
        if s > p and s > r:
            p -= 1
            s -= 1
            #pairs.append("PS")
            ns += 1
            continue
        p -= 1
        r -= 1
        #pairs.append("PR")
        np += 1

    t = []
    l = layer(nr, np, ns, False)
    #print(l)
    for c in l:
        if c == 'P':
            t.append('PR')
        elif c == 'R':
            if last:
                t.append('RS')
            else:
                t.append('SR')
        elif c == 'S':
            t.append('PS')
    return ''.join(t)

def rearrange(s):
    l = len(s)
    if l == 1:
        return s
    a, b = s[:l//2], s[l//2:]
    a = rearrange(a)
    b = rearrange(b)
    ab = a + b
    ba = b + a
    return min(ab, ba)


def solve(n, r, p, s):
    if abs(r - s) > 1 or abs(r - p) > 1 or abs(s - p) > 1:
        return "IMPOSSIBLE"
    l = layer(r, p, s, True)
    return rearrange(l)

    # pairs = []
    # while (r or p or s):
    #     if r > p and s > p:
    #         r -= 1
    #         s -= 1
    #         pairs.append("RS")
    #         continue
    #     if p > r and s > r:
    #         p -= 1
    #         s -= 1
    #         pairs.append("PS")
    #         continue
    #     if p > s and r > s:
    #         p -= 1
    #         r -= 1
    #         pairs.append("PR")
    #         continue
    #     if s > p and s > r:
    #         p -= 1
    #         s -= 1
    #         pairs.append("PS")
    #         continue
    #     p -= 1
    #     r -= 1
    #     pairs.append("PR")
    # return pairs


testcases = int(input())

for case_n in range(1, testcases+1):
    case_data = map(int, input().split())
    #case_data = input().split()
    print("Case #%i: %s" % (case_n, solve(*case_data)))
