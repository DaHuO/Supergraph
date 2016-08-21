import math

f=open('A-large.in', 'r')
g=open('outputsmall.txt','w')

def allZero(z):
    for i in z:
        if i!=0:
            return False
    return True

def findMax(z):
    sortedz=sorted(z, reverse=True)
    if sortedz[0]==sortedz[1]:
        firstMax=z.index(sortedz[0])
        z.remove(sortedz[0])
        secondMax=z.index(sortedz[1])+1
        z.insert(firstMax, sortedz[0])
    else:
        firstMax=z.index(sortedz[0])
        secondMax=z.index(sortedz[1])
    return firstMax, secondMax

def evacuatePeople(c, d):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return alphabet[c]+alphabet[d]

def evacuateLast(z):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return alphabet[z.index(1)]

def removefromz(z,c,d):
    z[c]=z[c]-1
    z[d]=z[d]-1
    return z

def evacuate(z):
    a = []
    while not allZero(z) and sum(z)>1:
        c, d = findMax(z)
        a.insert(0,evacuatePeople(c, d))
        z=removefromz(z, c, d)
    if sum(z)==1:   
        a.insert(0, evacuateLast(z))
    return a

data=[]
x=int(f.readline())
for a in range(x):
    y=int(f.readline())
    z=f.readline().strip().split(" ")
    for c in range(len(z)):
        z[c] = int(z[c])
    evacuatePlan = evacuate(z)
    answer = " ".join(evacuatePlan)
    print('Case #'+str(a+1)+': '+answer)
    g.write('Case #'+str(a+1)+': '+answer+'\n')



g.close()


