import sys
import collections


def flip(s, n):
    first = s[:n]
    last = s[n:]
    first = "".join(reversed(['-' if x=='+' else '+' for x in first]))
    return first+last

def solve(testcase):
    dist = {}
    q = collections.deque()
    data = sys.stdin.readline().strip()
    dist[data] = 0
    q.append(data)
    
    def expand(data):
        for i in range(1, len(data)+1):
            x = flip(data, i)
            if x in dist:
                continue
            dist[x] = dist[data]+1
            q.append(x)

    while q:
        x = q.popleft()
        if all(x=='+' for x in x):
            break
        expand(x)

    res = dist['+' * len(data)]

    print "Case #%d: %d" % (testcase, res)

for t in range(int(sys.stdin.readline().strip())):
    solve(t+1)
