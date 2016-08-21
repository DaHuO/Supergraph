from itertools import *

# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

T = input()

def npaths(n, g):
    s, t = 0, n - 1
    seen = {0}
    paths = [0 for i in range(n - 1)] + [1]
    def dfs(i):
        seen.add(i)
        if not paths[i]:
            paths[i] = sum(dfs(i) for i in g[i])
        return paths[i]
    dfs(0)
    # print paths
    return paths[0]
#
#
# def paths(n, target):
#
#     opts = [(x, y) for x in range(n) for y in range(n) if x < y]
#     for edg in powerset(opts):
#         adj = {i: [] for i in range(n)}
#         for x, y in edg:
#             adj[x].append(y)
#         if npaths(n, adj) == target:
#             edjs = set(edg)
#             return '\n'.join(''.join('1' if (x, y) in edjs else '0' for y in range(n)) for x in range(n))


def to_exc(B, left):
    # print 'to_exc', B, left
    if left == 0:
        return set([])
    else:
        b = bin(left - 1)[2:]
        b = '-' * (B - 2 - len(b)) + b
        # print b
        exc = set([(0, i) for i in range(1, B - 1) if b[i - 1] == '1'] + [(0, B - 1)])
        if B > 2 and left > 2 ** (B - 3):
            exc.update([(x + 1, y + 1) for x, y in to_exc(B - 1, left - 2 ** (B - 3)) ])
        return exc


def paths(B, M):
    b = bin(M)[2:]
    # print b
    exc = to_exc(B, 2 ** (B - 2) - M)

    edjs = set([(x, y) for x in range(B) for y in range(B) if x < y and (x, y) not in exc])
    n = B
    adj = {i: [] for i in range(n)}
    for x, y in edjs:
        adj[x].append(y)
    # print adj, exc
    assert npaths(B, adj) == M
    return '\n'.join(''.join('1' if (x, y) in edjs else '0' for y in range(n)) for x in range(n))

def solve(B, M):
    if M > 2 ** (B - 2):
        return 'IMPOSSIBLE'
    return 'POSSIBLE' + '\n' + paths(B, M)

for i in range(1, T + 1):
    B, M = map(int, raw_input().strip().split())
    # print B, M
    print 'Case #{}: {}'.format(i, solve(B, M))
