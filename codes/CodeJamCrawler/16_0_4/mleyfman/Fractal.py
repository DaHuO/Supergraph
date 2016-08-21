from sys import stdin

def solve(problem):
    K, C, S = map(int, problem.split())
    step = 0
    power = 1
    for i in range(C):
        step += power
        power *= K
    return [1 + i * step for i in range(K)]

T = int(stdin.readline())

for case in range(1, T + 1):
    print('Case #{}:'.format(case), *solve(stdin.readline().strip()))
