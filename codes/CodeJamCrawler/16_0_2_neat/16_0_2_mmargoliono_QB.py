import sys

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    line = sys.stdin.readline().strip()
    segment = 0
    char = ''
    for c in line:
        if c != char:
            segment += 1
            char = c
    if line[-1] == '+':
        segment -=1
    print("Case #{}: {}".format(i, segment))
