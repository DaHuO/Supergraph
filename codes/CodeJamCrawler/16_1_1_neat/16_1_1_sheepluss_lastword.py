from collections import deque

def lastword(ncase, s):
  lastword_seq = deque()
  lastword_seq.append(s[0])
  for i in xrange(1, len(s)):
    if s[i] >= lastword_seq[0]:
      lastword_seq.appendleft(s[i])
    else:
      lastword_seq.append(s[i])
  print "Case #%d: %s" % (ncase, "".join(list(lastword_seq)))

ncases = int(raw_input())
for i in xrange(1, 1+ncases):
  lastword(i, raw_input())
