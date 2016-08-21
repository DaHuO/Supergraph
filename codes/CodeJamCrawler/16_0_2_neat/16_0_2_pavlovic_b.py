import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    line = sys.stdin.readline().strip()
    cnt = 0
    for j in range(len(line) - 1):
        if line[j] != line[j + 1]:
            cnt += 1
    if line[-1] == '-':
        cnt += 1
    print "Case #%d: %d" % (i + 1, cnt)
