import random

def prime(x):
    i = 2
    while i*i <= x and i < 100:
        if x % i == 0:
            return i
        i += 1
    return -1

def is_good(x):
    sw = [prime(int(x,b)) for b in range(2,11)]
    if all(x>0 for x in sw):
        return sw

X = int(input())
N, J = map(int, input().strip().split())

print("Case #1:")

S = set()
for i in range(J):
    W = ''
    while len(W) != N or W in S:
        W = '1' + ''.join(random.choice("01") for _ in range(N-2)) + '1'
        if W in S: continue
        P = is_good(W)
        if P is not None:
            print(W, ' '.join(map(str, P)))
        else:
            W = ''
    S.add(W)
