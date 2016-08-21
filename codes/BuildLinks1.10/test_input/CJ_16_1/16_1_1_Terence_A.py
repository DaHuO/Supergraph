from collections import deque
def smax(s):
    q = deque()
    for c in s:
        if len(q) > 0 and c >= q[0]:
            q.appendleft(c)
        else:
            q.append(c)
    return ''.join(q)

t = int(raw_input())
for icase in range(1,t+1):
    s = raw_input().strip()
    print 'Case #%d: %s' % (icase,smax(s))