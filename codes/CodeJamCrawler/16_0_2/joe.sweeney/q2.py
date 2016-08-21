def findflippoint(i,pancakes,sign):
    while(pancakes[i]==sign):
        i+=1
        if i==len(pancakes):
            break
    return i

def done(pancakes):
    for side in pancakes:
        if side == "-":
            return False
    return True

def opposite(sign):
    if sign=='+':
        return '-'
    else:
        return '+'

def flip(i,pancakes):
    newcakes = []
    for n in range(i):
        sign = pancakes[n]
        newcakes.append(opposite(sign))
    for x in range(len(newcakes),len(pancakes)):
        newcakes.append(pancakes[x])
    return ''.join(newcakes)

def numFlips(pancakes):
    flips = 0
    while(not done(pancakes)):
        if pancakes[0]=='+':  #look for end of positves and flip
            i=findflippoint(0,pancakes,'+')
            pancakes = flip(i,pancakes)
        else: #find end of negatives and flip
            i=findflippoint(0,pancakes,'-')
            pancakes = flip(i,pancakes)
        flips+=1
    return flips

input = 'B-large.in'
f = open(input,'r')
out = open('out.txt','w')
case = 0
for line in f:
    if case == 0:
        case += 1
    else:
        print line
        out.write("Case #"+str(case)+": "+str(numFlips(line))+"\n")
        case+=1
