#!/usr/bin/env python3

#flip the N first pancakes of the S piles
# aka "the maneuver"
def flipPiles(S,N):
    toflip=S[:N]
    flipped=toflip.translate(str.maketrans("+-","-+"))
    flipped=flipped[::-1]
    return flipped+S[N:]


def main():
    inFile=open("dataset.txt",'r')
    outFile=open("output.txt",'w')
    print("Nombre de cas : "+str(int(inFile.readline())))
    case=0
    for line in inFile:
        case=case+1
        i=0#number of time we execute the maneuver
        P=line
        while '-' in P:#as long as there is a pankake that is not is the right position we work
            i=i+1
            # we assume that the optimal way is to switch the first chain of pancake
            #on the same side until that chain match the whole piles.
            #At that point, eather there are all on happy side and we are done or we have to flipped all of them
            c=P[0].translate(str.maketrans("+-","-+"))#seeking the first character which differ from the first one
            N=P.find(c)
            if N==-1:
                N=len(P)
            P=flipPiles(P,N)
        outFile.write("Case #"+str(case)+": "+str(i)+'\n');
    inFile.close()
    outFile.close()
    return

main()
