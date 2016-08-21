import sys
from collections import Counter
from copy import deepcopy

temp = sys.stdout
sys.stdout = open(r'C:\Users\palzle\Desktop\o.txt', 'w')

Q = open(r'C:\Users\palzle\Desktop\A-small-attempt0.in')
# Q = open(r'C:\Users\palzle\Desktop\t.txt')
T = int(Q.readline())

pool = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
pool = [Counter(s) for s in pool]
# print(pool)

def contains(large, small):
    for key in small:
        if large[key] < small[key]:
            return False
    return True

def q1(s):
    if not s:
        return []

    tooSmall = True
    for i in range(10):
        if contains(s, pool[i]):
            tooSmall = False
            subRes = q1(s - pool[i])
            if subRes is not None:
                return subRes + [i]

    if tooSmall:
        return None



for i in range(T):
    print('Case #%r:' % (i + 1), end=' ')
    s = Q.readline().strip()
    s = Counter(s)
    print(''.join(map(str, sorted(q1(s)))))
    # print(q1(n, data), end='')

sys.stdout = temp
