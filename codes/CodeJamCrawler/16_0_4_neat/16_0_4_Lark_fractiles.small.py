f = open("fractiles.small.in", "r")

T = int(f.readline())
K = []
C = []
S = []

for i in range(0, T):
    v = f.readline().split(" ")
    K.append(int(v[0]))
    C.append(int(v[1]))
    S.append(int(v[2]))

f.close()


f = open("fractiles.out", "w")

for m in range(0, T):
    f.write("Case #"+str(m+1)+": ")
    for i in range(0, K[m]):
        r = i * ( pow(K[m], C[m]) / K[m] ) + 1
        f.write(str(r) + " ")
    f.write("\n")
        
f.close()

print "done"
