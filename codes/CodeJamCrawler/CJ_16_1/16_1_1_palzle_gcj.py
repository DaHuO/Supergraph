import sys
from time import time
from itertools import product

temp = sys.stdout
sys.stdout = open(r'C:\Users\Spin\Desktop\o.txt', 'a')

# Q = open(r'C:\Users\Spin\Desktop\t.txt')
Q = open(r'C:\Users\Spin\Desktop\A-small-attempt0.in')
T = int(Q.readline())

def q1(s, res, j, k, l):
    if l == 1:
        res[k] = s[j]
        # print(res)
        return

    max_i = j+l-1
    for i in range(j+l-2, j-1, -1):
        if s[i] > s[max_i]:
            max_i = i
    # print(max_i)
    res[k] = s[max_i]
    # print(res)
    if max_i != j:
        q1(s, res, j, k+1, max_i-j)
    if max_i != j+l-1:
        # q1(s, res, max_i+1, k+max_i-j+1, j+l-1-max_i)
        res[k+max_i-j+1:k+l] = s[max_i+1:j+l]




for i in range(T):
    print('Case #%r:' % (i + 1), end=' ')
    # print('Case #%r:' % (i + 1))
    # q = map(int, Q.readline().split())
    q = list(Q.readline().strip())
    # print(q)
    res = [None] * len(q)
    # print(res)
    q1(q, res, 0, 0, len(q))
    res = ''.join(res)
    print(res)

sys.stdout = temp
