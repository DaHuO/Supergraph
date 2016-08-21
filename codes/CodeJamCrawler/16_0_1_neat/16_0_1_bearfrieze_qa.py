import fileinput

def solved(seen):
    for i in range(0, 10):
        if not i in seen: return False
    return True

def solve(N):
    if N == 0: return 'INSOMNIA'
    times = 1
    seen = {}
    while not solved(seen):
        n = N * times
        for key in str(n): seen[int(key)] = True
        times += 1
    return n

f = fileinput.input()
T = int(f.readline())

for case in range(1, T + 1):
    N = int(f.readline())
    print('Case #%d: %s' % (case, solve(N)))
