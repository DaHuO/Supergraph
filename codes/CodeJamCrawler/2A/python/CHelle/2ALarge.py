f = open("2AlInput.in","r")
T = int(f.readline())
import sys
##T = int(sys.stdin.readline())
n = ""
for i in range (0,T):
    N = f.readline().split()
##    N = sys.stdin.readline().split()
    R = int(N[1])
    P = int(N[2])
    S = int(N[3])
    N = int(N[0])
    r = (2**N/3-R)**2
    p = (2**N/3-P)**2
    s = (2**N/3-S)**2
    if (r > 1) or (s > 1) or (p > 1):
        t = "IMPOSSIBLE"
    else:
        p1 = "0"
        r1 = "1"
        s1 = "2"
        for j in range (0,N):
            if int(p1) < int(r1):
                p2 = p1+r1
            else: p2 = r1+p1
            if int(r1) < int(s1):
                r2 = r1+s1
            else: r2 = s1+r1
            if int(s1) < int(p1):
                s2 = s1+p1
            else: s2 = p1+s1
            p1 = p2
            r1 = r2
            s1 = s2
        if P == p2.count("0"):
            if R == p2.count("1"):
                w = p2
        if P == r2.count("0"):
            if R == r2.count("1"):
                w = r2
        if P == s2.count("0"):
            if R == s2.count("1"):
                w = s2
        t = ""
        for l in w:
            if l == "0":
                t = t+"P"
            if l == "1":
                t = t+"R"
            if l == "2":
                t = t+"S"
    n = n+"Case #"+str(i+1)+": "+t+"\n"
n = n.strip()
##print(n)
f.close()
f = open("2AlOutput.txt","w")
f.write(n)
f.close()
