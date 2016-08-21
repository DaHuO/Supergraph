import math

f=open('A-large.in', 'r')
g=open('outputsmall.txt','w')

data=[]
x=int(f.readline())
for a in range(x):
    data.append(int(f.readline()))

print(data)

def notAllIn(inside):
    for i in range(10):      
        if not(i in inside):
            return True    
    return False

def putInside(inside, currentNumber):
    for i in str(currentNumber):
        inside.append(int(i))
    return inside


for a in range(x):
    m=data[a]
    inside=[]
    i=1
    currentNumber = data[a]
    while (m != 0 and notAllIn(inside) and i < 1000001):
        currentNumber = i*m
        inside=putInside(inside, currentNumber)
        i=i+1
        print(i, currentNumber)
    if notAllIn(inside):
        print('Case #'+str(a+1)+': INSOMNIA')
        g.write('Case #'+str(a+1)+': INSOMNIA\n')
    else:
        print('Case #'+str(a+1)+': '+str(currentNumber))
        g.write('Case #'+str(a+1)+': '+str(currentNumber)+'\n')

g.close()


