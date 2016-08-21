import sys
sys.stdin = open("B-large.in","r")
sys.stdout = open("OP.txt","w")

from copy import deepcopy

sn = ["+","-"]

for asd in xrange(int(raw_input().strip())):
    pc = list(raw_input())
    ans = 0
    while (1):
        if not ("-" in pc): break
        elif not ("+" in pc):
            ans+=1
            break
        
        i = -1
        if pc[0]=="+" and "-" in pc: i = pc.index("-")
        elif pc[0]=="-" and "+" in pc: i = pc.index("+")

        npc = deepcopy(pc)
        for j in xrange(i):
            npc[j] = sn[not sn.index(pc[i-1])]
            i-=1
        pc = deepcopy(npc)        
        ans+= 1
            


    print "Case #%d: %d"%(asd+1,ans)



sys.stdout.close()

