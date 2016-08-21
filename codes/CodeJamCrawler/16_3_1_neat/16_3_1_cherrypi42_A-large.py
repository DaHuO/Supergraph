import math

fileout = open('A-large.out',"w")

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
with open('A-large.in') as file:
    T = int(file.readline())
    
    for case in range(1, T+1):
        N = int(file.readline())
        P = map(int,file.readline().split())
        total = sum(P)
        evac = ""
        while total > 0:
             dude = P.index(max(P))
             evac = evac + alpha[dude].upper()
             total -= 1
             P[dude] -= 1
             dude = P.index(max(P))
             if max(P) > (total) / 2:
                 evac = evac + alpha[dude].upper()
                 total -= 1
                 P[dude] -= 1
             evac = evac + " "    
        fileout.write("Case #" + str(case) + ": " + evac + "\n")
    
fileout.close()
