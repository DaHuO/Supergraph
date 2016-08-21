from collections import deque

def readint(): return int(raw_input())
def readlist(f): return map(f, raw_input().split())

T = readint()

for t in xrange(1, T + 1):
    S = list(raw_input())
    last_word = deque(S.pop(0), )

    for s in S:
        s = s.upper()

        if min(s, last_word[0]) == s and s != last_word[0]:
            last_word.append(s)
        else:
            last_word.appendleft(s)

    print "Case #%d: %s" % (t, ''.join(last_word))
