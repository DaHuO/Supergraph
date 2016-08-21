def flip(cakes):
    temp = str(cakes)
    temp = temp.replace('+','?')
    temp = temp.replace('-','+')
    temp = temp.replace('?','-')
    temp = list(temp)
    temp.reverse()
    temp = ''.join(temp)
    return temp
def maneuver(cakes):
    count = 0
    temp = list(cakes)
    temp.reverse()
    try:
        ind =temp.index('-')
        ind = len(cakes)-1-ind
    except ValueError:
        return 0
    #after ind all + if any, so cut it and do not touch it
    cakes = cakes[0:ind+1]
    if cakes[0]=='-':
        cakes=flip(cakes)
    else:
        ind = cakes.index('-')
        cakes = flip(cakes[0:ind])+cakes[ind:]
    return maneuver(cakes)+1
    
    
inf = open('B-large.in','r')
out = open('B-large.out','w')

T = int(inf.readline())
for i in range(1,T+1):
    cakes= inf.readline()
    out.write('Case #'+str(i)+': '+str(maneuver(cakes))+'\n')
out.close()
inf.close()
