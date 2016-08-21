import sys
import heapq

N=int(sys.stdin.readline())

def pot(s):
    p = 0
    for i in range(len(s) - 1):
        if s[i] !=  s[i + 1]:
            p += 1
    return p

def flip(x):
    return "".join(("+" if c == "-" else "-") for c in x[::-1])

for k in range(1, N + 1):
    stack = sys.stdin.readline().strip()
    
    g = {}
    q = [(pot(stack), 0, stack)]
    done = False
    while True:
        d, rd, candidate = q[0]
        heapq.heappop(q)

        if candidate not in g:
            g[candidate] = rd + 1

            if candidate == "+" * len(stack):
                print("Case #%d: %d" % (k, rd))
                break

            for i in range(1, len(candidate) + 1):
                nex = flip(candidate[0:i]) + candidate[i:]
                heapq.heappush(q, (pot(nex) + rd + 1, rd + 1, nex))
