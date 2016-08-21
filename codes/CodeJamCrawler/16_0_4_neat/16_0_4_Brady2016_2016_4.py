import math
'''
def fractal(tiles,c):
    newg=""
    result=tiles[:]
    for index in range(len(tiles)):
        newg=newg+"G"
    for index in range(c-1):
        result=result.replace('G','g')
        result=result.replace('L',tiles)
        result=result.replace('g',newg)
    return result

def getall(k):
    result=[]
    for index in range(k):
        inre=""
        for inside in range(k):
            if inside==index:
                inre=inre+"G"
            else:
                inre=inre+"L"
        result.append(inre);
    return (result)
def doit(K,C,S):
    minanswer=K-C+1
    if minanswer<1:
        minanswer=1
    if minanswer>S:
        return "IMPOSSIBLE"
    if C>K:
        C=K
    all=getall(K)
    
    for index in range(len(all)):
        all[index]=fractal(all[index],C)
        #print(all[index])  
    result=[0 for i in range(len(all[0]))]    
    for outside in range(len(all[0])):
        for inside in range(len(all)):
            if all[inside][outside]=="L":
                result[outside]=result[outside]+1
    answernum=0
    result2=""
    for index in range(len(result)):
        if answernum<minanswer and result[index]==K-C:
            answernum=answernum+1
            result2=result2+str(index+1)+" "
    return result2
'''

def doit2(K,C,S):
    minanswer=K-C+1
    if minanswer<1:
        minanswer=1
    if minanswer>S:
        return "IMPOSSIBLE"
    if C>K:
        C=K
    
    first=0
    for index in range(1,C):
        first=int(first+math.pow(K,C-1-index)*index)
    first=first+1
    result2=""
    for ans in range(minanswer):
        result2=result2+str(first+ans)+" "
    return result2


file = open("a")
T = file.readline()
all_the_text=[]

for num in range(1,int(T)+1):
    final=file.readline().rstrip().split(' ')
    
    newfinal=doit2(int(final[0]),int(final[1]),int(final[2]))
    temstr='Case #'+str(num)+': '+str(newfinal)+'\n'
    all_the_text.append(temstr)
    
file_object = open('thefile.txt', 'w+')
file_object.writelines(all_the_text)
file_object.close( )

