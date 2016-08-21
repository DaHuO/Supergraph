import sys, copy;
def ar(r,a,b,c):
    r.append([a+1,b+1,c+1])
def solve():
    jp = j*p
    js = j*s
    ps = p*s
    m = min(jp*min(s,k),js*min(p,k),ps*min(j,k))
    r = []
    if jp*min(s,k) == m:
        for a in range(j):
            for b in range(p):
                for c in range(min(s,k)):
                    ar(r,a,b,(a+b+c)%s)
        return [m,r]
    if js*min(p,k) == m:
        for a in range(j):
            for b in range(min(p,k)):
                for c in range(s):
                    ar(r,a,(a+b+c)%p,c)
        return [m,r]
    if ps*min(j,k) == m:
        for a in range(min(j,k)):
            for b in range(p):
                for c in range(s):
                    ar(r,(a+b+c)%j,b,c)
        return [m,r]

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        j,p,s,k=map(int,f.readline().split())
        x = solve()
        file.write(str(x[0])+ "\n")
        for y in x[1]:
            file.write(" ".join(map(str,y))+ "\n")
file.close()            








