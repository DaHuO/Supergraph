from sys import *
T = input()

def toDig(n):
    return [int(x) for x in str(n)]
for I in range(int(T)):
    n = int(input())
    stdout.write("Case #"+str(I+1)+": ")
    if n==0:
        stdout.write("INSOMNIA\n")
    else:
        digs = set([])
        i=1
        while(len(digs)<10):
            digs = digs.union(toDig(i*n))
            i+=1
        stdout.write(str((i-1)*n)+"\n")
            
