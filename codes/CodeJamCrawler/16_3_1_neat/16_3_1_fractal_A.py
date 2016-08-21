T = int(raw_input())

for t in range(1,T+1):
        N = int(raw_input())
        P = [(int(y), chr(x)) for (x,y) in zip(range(ord('A'), ord('Z')+1), raw_input().split())]
        P.sort(reverse=True)
        outq = []
        while len(P)>1:
                #print P
                outq.append(P[0][1]+P[1][1]) 
                P[0] = (P[0][0]-1, P[0][1])
                P[1] = (P[1][0]-1, P[1][1])
                while len(P) and P[0][0] == 0:
                        del P[0]
                P.sort(reverse=True)
        if len(P):
                outq.insert(-1, P.pop()[1])
        print "Case #%d: %s" % (t, ' '.join(outq))
        
