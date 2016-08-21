from collections import defaultdict
import numpy as np

asca = 65

def toascii(num):
    return str(unichr(asca+num))

def solve():
    sd = dict( [ (toascii(i),e) for i,e in enumerate(s) ] )
    ks = sd.keys()

    sol = []

    global S
    while S>2:
        vals = np.array(sd.values(),float)
        SS = sum(vals)
        assert np.all(vals/SS <= 0.5), (vals/SS, sd)
        # print vals/SS, sd
        ks.sort(key=lambda x: -sd[x])
        d1 = ks[0]
        d2 = ks[1]
        if sd[d1] == sd[d2] and not (sd[d1] == 1 and sd[d2] == 1 and S==3):
        # km = max(ks,key=lambda x: sd[x])
            sol.append(d1+d2)
            sd[d1]-=1
            sd[d2]-=1
            S-=2
        else:
            sol.append(d1)
            sd[d1]-=1
            S-=1


    vals = np.array(sd.values(),float)
    SS = sum(vals)
    assert np.all(vals/SS <= 0.5), (vals/SS, sd)
    # print vals/SS, sd
    
    ks.sort(key=lambda x: -sd[x])
    sol.append(''.join(ks[:S]))

    # print sd

    return ' '.join(sol)


T = int(raw_input())

for i in range(T):
  N = int(raw_input())
  # s = raw_input()
  s = map(int,raw_input().split())
  S = sum(s)
  sol = solve()
  print "Case #%d: %s"%(i+1,sol)
