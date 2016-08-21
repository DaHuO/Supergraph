f = open("C:\Users\Himan\Desktop\Downloads\B-small-attempt0.in","r")
other = open("C:\Users\Himan\Desktop\output3.txt","w")


t = int(f.readline())

def alter(s):
    newS = ''
    for char in s:
        if char=='+':
            newS+='-'
        else:
            newS+='+'
    return newS        

def flip(i,x):
    first = alter(x[:i][::-1])
    if x[i:]:
        first+=x[i:]
    return first    

def calculate(start, n):
    level={}
    visited=[]
    q = [start]
    level[start]=0
    last = '+'*n
    while q:
        x = q.pop(0)
        if x == last:
            return level[x]
        else:
            for i in xrange(n):
                newX = flip(i+1, x)
                if newX not in visited:
                    level[newX]=level[x]+1
                    visited.append(newX)
                    q.append(newX)


for i in xrange(t):
    s = f.readline().strip()
    other.write("Case #"+str(i+1)+": "+str(calculate(s, len(s)))+"\n")

other.close()
f.close()
            
            
            
