fo = open("D-small-attempt0.in", "r")
fout=open("output2.txt","w")
T=int(fo.readline())
for i in range(T):
    K,C,S=map(int,fo.readline().split())
    if(S>=K):
        fout.write("Case #%d: "%(i+1))
        for j in range(K):
            fout.write("%d "%(j+1))
        fout.write('\n')
    else:
        fout.write("Case #%d: %s\n"%(i+1,"IMPOSSIBLE"))
fo.close()
fout.close()
