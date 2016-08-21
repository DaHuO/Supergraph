# Google Code Jam 2016 - Qualification Round
# Problem B

import itertools
from Queue import Queue

def bfs(s):
    seen = set()
    q = Queue()
    seen.add(s)
    q.put((s, 0))

    while not q.empty():
        s,c = q.get()
        if s.count('+') == len(s):
            return c
        for i in xrange(1, len(s) + 1):
            x = s[:i][::-1].replace('+', '.').replace('-', '+').replace('.', '-') + s[i:]
            if x not in seen:
                q.put((x, c + 1))
                seen.add(x)

    return None

def nomames(s):
    s = ''.join([ str(elem) for elem,group in itertools.groupby(s) ])
    return len(s) if s[-1] == '-' else len(s) - 1

for case in xrange(int(raw_input())):
    #print 'Case #%u: %u' % (case + 1, bfs(raw_input()))
    print 'Case #%u: %u' % (case + 1, nomames(raw_input()))
