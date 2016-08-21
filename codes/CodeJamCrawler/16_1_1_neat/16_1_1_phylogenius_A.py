import sys

for t in range(1, int(sys.stdin.readline()) + 1):
    word = sys.stdin.readline().strip()
    wip = ''
    for c in word:
        wip = max(c + wip, wip + c)
    print('Case #{}: {}'.format(t, wip))
