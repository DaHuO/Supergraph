R = []
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open("input.txt","r")
T = int(f.readline())
for k in range(T):
    print(k)
    s = f.readline()
    n = len(s)
    r = s[0]
    d = A.index(s[0])
    for i in range(1,n):
        if A.count(s[i]):
            e = A.index(s[i])
            if e >= d:
                r = s[i] + r
                d = e
            else:
                r = r + s[i]
    R = R + [r]       
f.close()
f = open("output.txt","w")
for k in range(T):
    f.write("Case #"+str(k+1)+": "+str(R[k])+"\n")
f.close()

    
