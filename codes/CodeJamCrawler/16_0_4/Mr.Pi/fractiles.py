import sys

def gen_all(K):
    if K == 1: return ["G", "L"]
    ans = []
    for x in gen_all(K-1):
        ans.append(x+"G")
        ans.append(x+"L")
    return ans

def expand(seq, C):
    if C == 1: return seq
    """
    oldseq = expand(seq, C-1)
    newseq = ""
    for c in oldseq:
        if c == 'L':
            newseq += seq
        else:
            newseq += "G"*len(seq)
    return newseq
    """
    goldrep = "G"*len(seq)
    return "".join([seq if c == 'L' else goldrep for c in expand(seq, C-1)])

def test(K, C):
    startall = gen_all(K)
    for x in startall: print(x)
    print("")
    for x in startall:
        print(expand(x, C))
        

if __name__ == "__main__":
    f = open(sys.argv[1])
    T = int(f.readline().strip())
    for i in xrange(1, T+1):
        K, C, S = map(int, f.readline().strip().split())
        if K == 1:
            print("Case #"+str(i)+": 1")
            continue
        elif C == 1:
            if K != S:
                 print("Case #"+str(i)+": IMPOSSIBLE")
            else:
                 ans = range(1,K+1)
                 print("Case #"+str(i)+": "+" ".join(map(str, ans)))
            continue
        elif S == 1:
            print("Case #"+str(i)+": IMPOSSIBLE")
            continue
        elif S == K:
            finallen = K**C
            seglen = finallen/S
            ans = range(1,finallen,seglen)
            print("Case #"+str(i)+": "+" ".join(map(str, ans)))
        else:
            raise Exception("Not implemented yet")
            allstart = gen_all(K)
            #for i in xrange(2**K):
            #
            # dynamic memo G -> GGG -> GGGGGG etc.   
            print("Case #"+str(i)+": "+" ".join(map(str, ans)))
