import numpy as np

ind = open("D-small-attempt0.in", "r")
outd = open("D-small-attempt0.out", "w")

T = int(ind.readline())

for i in range(1, T+1):
    K, C, S = map(int, ind.readline().split())
    
    output = ""
    
    for j in range(1,S+1):
        output = output + " " + str(j)
    
    print("Case #"+str(i)+":"+output+"\n")
    outd.write("Case #"+str(i)+":"+output+"\n")

ind.close()
outd.close()

