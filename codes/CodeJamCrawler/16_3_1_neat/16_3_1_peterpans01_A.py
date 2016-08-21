def solve(N,P):
    res = []
    sm = sum(P)
    while sm:
        ind = sorted(range(len(P)),key =lambda k: P[k], reverse=True)
        if max(P[ind[0]] - 2,P[ind[1]]) <= (sm - 2)/2:
            res.append(str(chr(ord('A')  + ind[0]))*2)
            P[ind[0]] = max(P[ind[0]]- 2,0)
            sm-=2
        elif max(P[ind[0]] - 1,P[ind[1]]-1, P[ind[2]]) <=(sm - 2)/2:
            res.append(str(chr(ord('A')+ ind[0]) + chr(ord('A') + ind[1])))
            P[ind[0]] = max(P[ind[0]]- 1,0)
            P[ind[1]] = max(P[ind[1]]- 1,0)
            sm-=2
        else:
            res.append(str(chr(ord('A') + ind[0])))
            P[ind[0]] = max(P[ind[0]]- 1,0)
            sm-=1
    return res
            


def test():
    print solve(3,[1,1,2] + [0]*23)
                
def main():
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        N = input()
        l = [int(_) for _ in raw_input().split()]
        P = l + [0]*(26-len(l))
        res = " ".join(solve(N,P))
        print("Case #%i: %s" % (caseNr, res))
    

if __name__ == "__main__":
    #test()
    main()
    
    
        
