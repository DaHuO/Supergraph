filename = "/home/andybozhko/Downloads/codejam/D/D-small-attempt0"

fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())

for T in xrange(trials):
    [K, C, S] = map(int, fin.readline().split())
    
    
    pos = [i+1 for i in range(K)]
    if (K > 1) and (C > 1):
        pos.pop(0)
    if (S >= len(pos)):
        fout.write("Case #{0}: ".format(T+1)+" ".join(map(str,pos))+"\n")
    else:
        fout.write("Case #{0}: ".format(T+1)+"IMPOSSIBLE\n")
                    
fin.close()
fout.close()