def divisor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return n

def proof(s):
    p = []
    for base in range(2, 10 + 1):
        n = int(s, base)
        d = divisor(n)
        if d == n:
            return None
        p.append(d)
    return p

def solve(N, J):
    padded_binary = '{{:0{}b}}'.format(N - 2)
    for i in range(2 ** (N - 2)):
        s = '1' + padded_binary.format(i) + '1'
        p = proof(s)
        if not p:
            continue
        print(s, ' '.join(map(str, p)))
        J -= 1
        if J == 0:
            break

T = int(input())
for t in range(T):
    N, J = map(int, input().split())
    print('Case #{}:'.format(t + 1))
    solve(N, J)
