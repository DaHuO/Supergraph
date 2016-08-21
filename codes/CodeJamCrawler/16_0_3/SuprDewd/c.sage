import random

n = 32
j = 500

def fst(n):
    return [1] + [0]*(n-2) + [1]

def get(n):
    return [1] + [ random.randint(0,1) for _ in range(n-2) ] + [1]

def nxt(arr):
    arr = list(arr)
    at = len(arr)-2
    carry = 1
    while carry == 1 and at > 0:
        here = arr[at] + carry
        arr[at] = here % 2
        carry = here // 2
        at -= 1
    assert carry == 0 or at > 0
    return arr

def parse(arr, b):
    res = 0
    for x in arr:
        res = res * b + x
    return res

print 'Case #1:'
here = fst(n)
cnt = 0
while True:
    ok = True
    for b in range(2,11):
        val = parse(here, b)
        if is_prime(val):
            ok = False
    if ok:
        cnt += 1

        print ''.join(map(str,here)), ' '.join(map(str,[ factor(parse(here, b))[0][0] for b in range(2,11) ]))
        if cnt == j:
            break
    here = nxt(here)

