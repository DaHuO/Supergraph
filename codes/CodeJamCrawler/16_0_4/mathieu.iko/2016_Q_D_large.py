import sys
import math


DEBUG=True if len(sys.argv) > 1 else False
def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)



def solve(K, C, S):
    if S < K/C:
        return "IMPOSSIBLE"
    students = []
    for S in range(math.ceil(K/C)):
        debug(S, list(zip(range(S*C+1, min(S*C+C+1, K+1)), range(C-1, -1, -1))))
        students.append(1 + sum([(n-1) * (K**X) for n,X in zip(range(S*C+1, min(S*C+C+1, K+1)), range(C-1, -1, -1))]))
    return ' '.join(map(str, students))


for case in range(1, int(sys.stdin.readline())+1):
    K, C, S = map(int, sys.stdin.readline().split())

    debug("K:", K, "; C:", C, "; S:", S)

    solution = solve(K, C, S)

    print("Case #{0}: {1}".format(case, solution))

