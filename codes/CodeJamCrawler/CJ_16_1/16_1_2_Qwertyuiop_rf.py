import sys



f = open(sys.argv[1], "r")
F = open(sys.argv[1]+".output","w")

T = int(f.readline())
for i in (range(T)):
    N = int(f.readline())
    m = {}
    for j in range(2*N-1):
        L = f.readline()
        L = L.rstrip()
        L = L.split(" ")
        L = map(int, L)
        for n in L:
            try: m[n]+=1
            except: m[n]=1
    ans=[]
    for k in m.keys():
        if m[k]%2!=0:
            ans.append(k)
    ans.sort()
    if len(ans)!=N:
        raise Exception()
    ans = map(str, ans)
    ans = " ".join(ans)

    F.write("Case #")
    F.write(str(i+1))
    F.write(": ")
    F.write(ans)
    F.write("\n")
F.close()