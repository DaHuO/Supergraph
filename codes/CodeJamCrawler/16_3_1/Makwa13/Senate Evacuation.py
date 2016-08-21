#-------------------------------------------------------------------------------
# Name:        Senate Evacuation
# Purpose:
#
# Author:      udonko
#
# Created:     08/05/2016
# Copyright:   (c) udonko 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import string

arrayParty=[ch for ch in string.ascii_uppercase]

def ressolve(n,parties):
    result=[]
    num = sum(parties)

    while num > 0:
        idx = parties.index(max(parties))
        parties[idx] -=2
        num-=2
        halfnum = num // 2
        maxp=max(parties)
        idx2 = parties.index(maxp)
        if parties[idx2] > halfnum:
            parties[idx]+=1
        #    num+=1
            parties[idx2] -= 1
            idx3=parties.index(max(parties))
            if parties[idx3] > halfnum:
                result.append(arrayParty[idx])
                parties[idx2] +=1
                num +=1
            else:

                result.append(arrayParty[idx]+arrayParty[idx2])
        else:
            result.append(arrayParty[idx]*2)
        #print(str(parties))
    return result
def main():
    with open("A-small-attempt1 (1).in","r") as inputfile:
        with open("output.txt","w") as outfile:
            t=int(inputfile.readline())
            for testnum in range(t):
                n=int(inputfile.readline())
                parties = list(map(int, inputfile.readline().split()))
                result = ressolve(n,parties)
                outtxt = "Case #{0}: {1}\n".format(testnum+1, " ".join(result))
                #sys.stdout.write(outtxt)
                outfile.write(outtxt)
if __name__ == '__main__':
    main()
