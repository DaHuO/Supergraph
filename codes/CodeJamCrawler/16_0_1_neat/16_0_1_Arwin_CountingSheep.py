__author__ = 'Arwin'
import sys
fn= 'A-large.in'
f = open( fn )
ansf=open("ans.txt", "w")

def countingsheep(n):
    if n==0:
        return 'INSOMNIA'
    dgs= range(0,10)
    i=0
    while len(dgs)>0:
        i+=1
        chars= str(n*i)
        for char in chars:
            if len(dgs)==0:
                break
            thisdgt= int(char)
            if thisdgt in dgs:
                dgs.remove(thisdgt)
    return n*i

T= int(f.next())
for i in xrange(1,T+1):
    nn= int(f.next())
    ansf.write( 'Case #{0}: {1}\n'.format(i, countingsheep(nn)) )
