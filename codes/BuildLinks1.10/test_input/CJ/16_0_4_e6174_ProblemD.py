import math
f = open("dsmall.in", "r")
outf = open("out.txt", "w")

T = int(f.readline())

for t in range(1, T+1):
    outf.write("Case #" + str(t) + ": ")
    list = f.readline().strip().split()
    K = int(list[0])
    C =  int(list[1])
    S = int(list[2])
    
    n = K**C
    d = K**(C-1)
    for i in range(1, n+1, d):
        outf.write(str(i)+" ")
    outf.write("\n")
outf.close()


    
    