from collections import Counter

import gcj

def get_case(lines):
    n = int(next(lines))
    p = [int(x) for x in next(lines).split()]
    c = {chr(i + ord('A')): x for i,x in enumerate(p)}
    return Counter(c)

def no_majority(c):
    # print('maj', c)
    if not c:
        return False
    t = sum(c.values())
    m = c.most_common(1)[0]
    return m[1]/t <= .5


def pop(c):
    # mc = c.most_common(1)[0]
    #     p, n = c.items(0)
    #     r = p
    #     c[p] -= 1
    #     if n > 1:
    #         c[p] -= 1
    if sum(c.values()) in (1, 2):
        r = ''.join(c.elements())
        c -= c
        return r

    mc = c.most_common(2)
    a = mc[0]
    choices = [{a[0]: 1}]
    if a[1] > 1:
        choices = [{a[0]:2}] + choices

    if len(c) > 1:
        b = mc[1]
        choices = [{a[0]: 1, b[0]: 1}] + choices

    # print('ch', choices)

    for ch in choices:
        ch = Counter(ch)
        if no_majority(c - ch):
            c -= ch
            return ''.join(ch.elements())


def solve(c):
    res = []
    while c:
        # print('pop', c)
        res.append(pop(c))
        # print('c', c)
        # print('res', res)
    
    return ' '.join(res)

if __name__ == '__main__':
    gcj.main(solve, get_case)
