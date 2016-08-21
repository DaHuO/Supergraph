import sys
from collections import deque

def swap(s):
    res = ''
    for c in s:
        if c == '+':
            res += '-'
        else:
            res += '+'
    return res

with open(sys.argv[1]) as infile:
    with open(sys.argv[1]+".out", 'w') as outfile:
        nt = int(infile.readline())
        for t in range(1,nt+1):
            s = infile.readline().strip()
            n = len(s)
            v = set()
            b = {s : 0}
            curr = s
            q = deque([s])
            goal = '+' * n 
            print ":" + s
            while len(q) != 0: 
                curr = q.popleft()
                print curr
                if curr == goal:
                    break
                if curr in v:
                    continue
                v.add(curr)
                for f in range(1, n+1):
                    next = swap(curr[:f]) + curr[f:]
                    if next in v:
                        continue
                    q.append(next)
                    b[next] = b[curr]+1
            if curr != goal:
                outfile.write('Case #' + str(t) + ': ' + 'IMPOSSIBLE\n')
            else:
                outfile.write('Case #' + str(t) + ': ' + str(b[goal]) + "\n")



