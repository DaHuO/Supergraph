from collections import deque

T = int(input())
Ss = [input() for _ in range(T)]

for i,S in enumerate(Ss):
    LS=deque()
    for w in S:
        if len(LS)==0: LS.append(w)
        elif ord(w) >= ord(LS[0]): LS.appendleft(w)
        else: LS.append(w)
    print("Case #%d: %s"%(i+1,''.join(LS)))