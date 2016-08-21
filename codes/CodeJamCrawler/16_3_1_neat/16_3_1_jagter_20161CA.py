import numpy as np

ind = open("A-large.in", "r")
outd = open("A-large.out", "w")

T = int(ind.readline())

def majority(P):
    if P.sum() == 0:
        return 0
    return P.max()/P.sum()

for i in range(1, T+1):
    N = int(ind.readline())
    P = map(int,ind.readline().split())
    P = np.array(P)
    
    evac = []
    evacString = ""
    counter = 0
    
    while P.max()>0:
        mostidx = P.argmax()
        evac.append(mostidx)
        counter += 1
        P[mostidx] -= 1
        
        mostidx = P.argmax()
        evac.append(mostidx)
        counter += 1
        P[mostidx] -= 1
        
        if majority(P) > 0.5:
            P[mostidx] += 1
            evacString += chr(65+evac[0])+" "
            counter = 0
            evac = []
            if majority(P) > 0.5:
                print "error! " 
                print P
            continue
        if P.sum()==1:
            evacString += chr(65+evac[0])+" "
            counter = 0
            evac = []
            break
        if counter==2:
            evacString += chr(65+evac[0])+chr(65+evac[1])+" "
            counter=0
            evac = []
    
    #print evacString    
    
    print("Case #"+str(i)+": "+evacString+"\n")
    outd.write("Case #"+str(i)+": "+evacString+"\n")

ind.close()
outd.close()

