import sys, copy;

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def step():
    m1 = 0
    m2 = 0
    p1 = -1
    p2 = -1
    total = 0
    for i in range(n):
        total += p[i]
        x = p[i]
        #print(x,file=sys.stderr)
        if x > m1:
            if m1 > 0:
                m2 = m1
                p2 = p1
            m1 = x
            p1 = i
        else:
            if x  > m2:
                m2 = x
                p2 = i
    #print("p",p,"p1=",p1,"p2=",p2,"m1=",m1,"m2=",m2,file=sys.stderr)
    if total == 3 or total == 1:
        p[p1] -= 1
        return [total-1,alphabet[p1]]
    if m1 > m2:
        p[p1] -= 2
        return [total-2,alphabet[p1] + alphabet[p1]]
    else:
        #print("p1=",p1,"p",p,file=sys.stderr)
        p[p1] -= 1
        p[p2] -= 1
        return [total-2,alphabet[p1] + alphabet[p2]]
def solve():
    x = step()
    #print(x,x[0],file=sys.stderr)
    y = []
    while x[0] > 0:
        y.append(x[1])
        x = step()
        #print("x=",x,"x0=",x[0],"y=",y,file=sys.stderr)
    y.append(x[1])
    return " ".join(y)

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        n = int(f.readline())
        p = f.readline().split()
        p = [int(x) for x in p]
        #print(p,file=sys.stderr)
        
        file.write(str(solve()) + "\n")
file.close()            








