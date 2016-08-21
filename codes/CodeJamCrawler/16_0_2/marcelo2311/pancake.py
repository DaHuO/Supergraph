def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()

def turn(l, i):
    for k in range(0, i+1):
        #print k
        if l[k] == "-":
            l[k] = "+"
        elif l[k] == "+":
            l[k] = "-"
    #print l        
    return l            

for _t in range(_T):
    D = raw_input()
    S = list(D)
    max = len(S)
    S.append("0")  
    r = 0
    for i in range(max):
        if "-" in S:
            for j in range(max):
                if "-" in S:
                    if S[j] == "-" and (S[j+1] == "+" or S[j+1] == "0"):
                        #print S, j
                        S = turn(S, j)
                        r = r+1
                else:
                    break     
        else:
            break               
    print 'Case #%i:'%(_t+1), r
