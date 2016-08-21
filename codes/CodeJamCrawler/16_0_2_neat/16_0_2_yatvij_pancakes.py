f = open('pancakesin.txt','r')

t = int(f.readline())  # read a line with a single integer


smallest = 10000000

    
def flip(pancakelist,flipcount):
    pancakelistend = pancakelist[flipcount::]
    
    pancakelistpart = pancakelist[0:flipcount]
    pancakelistpart = pancakelistpart[::-1]
    pancakelistpart = pancakelistpart.replace('+','1')
    pancakelistpart = pancakelistpart.replace('-','0')
    pancakelistpart = pancakelistpart.replace('0','+')
    pancakelistpart = pancakelistpart.replace('1','-')
    finallist = pancakelistpart+pancakelistend
    return finallist
    

def findfastest2(pancakelist):
    solved = False
    comboLists = []
    comboRow = 0
    idealString = '+' * len(pancakelist)
    if(pancakelist == idealString):
        return 0
    comboLists.append([pancakelist])
    while(solved==False):
        comboRow+=1
        comboLists.append([])
        for element in comboLists[comboRow-1]:
            for n in range(len(pancakelist)):
                comboLists[comboRow].append(flip(element,n+1))
        comboLists[comboRow] = list(set(comboLists[comboRow]))
        for element in comboLists[comboRow]:
            if(element==idealString):
                solved = True
                return comboRow     
'''for i in xrange(1, t+1):
    pancakeList = (f.readline())
    result = findfastest2(str(pancakeList[0:-1:1]))
    g = open('pancakesout.txt','w').close()
    g = open('pancakesout.txt','a')
    g.write( "Case #{}: {}\n".format(i, result))
g.close()
f.close()'''

def findfastest3(pancakelist):
    currentindex=0
    idealCase = '+'*len(pancakelist)
    notsoideal = '-'*len(pancakelist)
    if(pancakelist==notsoideal):
        return 1
    if(pancakelist==idealCase):
        return 0
    if pancakelist[currentindex]=='+':
        while(pancakelist!=idealCase):
            currentindex+=1
            pancakelist = flip(pancakelist,pancakelist.find('-'))
            print pancakelist
            if '+' not in pancakelist:
                return currentindex+1
            pancakelist = flip(pancakelist,pancakelist.find('+'))
            currentindex+=1
            print pancakelist
            
        return currentindex
    else:
        while(pancakelist!=idealCase):
            currentindex+=1
            pancakelist = flip(pancakelist,pancakelist.find('+'))
            if '-' not in pancakelist:
                return currentindex
            currentindex+=1
            pancakelist = flip(pancakelist,pancakelist.find('-'))
            
            if '+' not in pancakelist:
                return currentindex+1
g = open('pancakesout.txt','w').close()         
for i in xrange(1, t+1):
    pancakeList = (f.readline())
    print pancakeList
    result = findfastest3(str(pancakeList[0:-1:1]))
    print result

    g = open('pancakesout.txt','a')
    g.write( "Case #{}: {}\n".format(i, result))
g.flush()
g.close()
f.close()