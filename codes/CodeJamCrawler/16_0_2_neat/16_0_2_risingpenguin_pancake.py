import math

f=open('B-large.in', 'r')
g=open('outputsmall.txt','w')

data=[]
x=int(f.readline())
for a in range(x):
    data.append(f.readline().strip())

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
    m = data[a]
    inside = [m[0]]
    for i in range(len(m)-1):
        if m[i+1] != m[i]:
            inside.append(m[i+1])
    if m[-1] == "+":
        print('Case #'+str(a+1)+': '+str(len(inside)-1))
        g.write('Case #'+str(a+1)+': '+str(len(inside)-1)+'\n')
    else:
        print('Case #'+str(a+1)+': '+str(len(inside)))
        g.write('Case #'+str(a+1)+': '+str(len(inside))+'\n')

g.close()


