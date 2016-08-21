from collections import defaultdict

cache = dict()

choices = ['P','R','S']

def who_wins(lft,rt):
  if lft == rt:
    return None
  if lft == 'P' and rt == 'S':
    return 'S'
  if lft == 'S' and rt == 'R':
    return 'R'
  if lft == 'R' and rt == 'P':
    return 'P'
  return who_wins(rt, lft)

def best_tournament(N, R, P, S, winner):

  if(N == 1):
    if winner == "R":
      if R > 0:
        return "R"
      else:
        return None
    if winner == "P":
      if P > 0:
        return "P"
      else:
        return None  
    if winner == "S":
      if S > 0:
        return "S"
      else:
        return None
  
  if (R,P,S,winner) in cache:
    return cache.get((R,P,S,winner))
  
  best = None
  for lft in choices:
    for rt in choices:
      win = who_wins(lft, rt)
      if(win is not None and win == winner):
        for rs in xrange(min(R, N/2)+1):
          for ps in xrange(min(P,N/2-rs)+1):
            ss = N/2-ps-rs
            if(ss >= 0 and ss <= S):
              bl = best_tournament(N/2, rs, ps, ss, lft)
              if bl is not None:
                br = best_tournament(N/2, R-rs, P-ps, S-ss, rt)
              if bl is not None and br is not None:
                next = bl + br
                if best is None or next < best:
                  best = next
  cache[(R,P,S,winner)] = best
  return best
    
def do_case(N, R, P, S):
  global cache
  cache = dict()
  bv = None
  for ch in choices:
    gv = best_tournament(N, R, P, S, ch)
    if(bv is None or (gv is not None and gv < bv)):
      bv = gv
  if bv is None:
    return "IMPOSSIBLE"
  
  return bv
    
f = open("A-small-attempt0.in").read()
lines = f.split("\n")
T = int(lines[0])
i=1
out=""
for line in lines[1:]:
  if len(line) > 0:
    parts = line.split(" ")
    out+="Case #%d: %s\n" % (i, do_case(2**int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])))
    i+=1
  
open("A-small.out","w").write(out)
