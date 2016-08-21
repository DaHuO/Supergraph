#coding:utf-8
def readFile():
    file=open("B-small-attempt0.in","r")
    T=file.readline()
    content=file.readlines()
    content=[x.split("\n")[0] for x in content]
    file.close()
    return T,content
def cntCon(x):
    if(len(x)==1):
        if(x[0]=='-'):return 1
    firstD=len(x)-1
    cnt=0
    for i in reversed(range(0,len(x))):
        if(x[i]=='-'):
            firstD=i
            cnt+=1
            break
    for i in reversed(range(1,firstD+1)):
        if(not(x[i]==x[i-1])):
            cnt+=1
    return cnt
def RoP(T,content):
    res=[]
    for x in range(0,int(T)):
        res.append(cntCon(content[x]))
    return  res
def writeFile(res):
    file=open('RoP_result.in','w')
    for i in range(0,len(res)):
        file.write("Case #{0}: {1}\n".format(i+1,res[i]) )
    file.close()
if __name__ == '__main__':
    T,content=readFile()
    res=RoP( T,content)
    writeFile(res)