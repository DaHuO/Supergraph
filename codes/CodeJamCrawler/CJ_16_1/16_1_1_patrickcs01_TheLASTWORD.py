#coding:utf-8
def readFile():
    file=open('A-small-attempt1.in','r')
    T=file.readline()
    S=file.readlines()
    S=[x.split("\n")[0] for x in S]
    file.close()
    return  T,S
def F(T,S):
    result=[]

    for x in xrange(0,len(S)):
        k=S[x]
        s=" "
        for y in k:
            if(y>=s[0]):
                s=y+s
            else:
                s+=y
        s=s.split(" ")[0]+s.split(" ")[1]
        result.append(s)
    return result
def writeFile(res):
    file=open('A_result.in','w')
    for i in range(0,len(res)):
        file.write("Case #{0}: {1}\n".format(i+1,res[i]) )
    file.close()
if __name__ == '__main__':
  T,S=readFile()
  result=F(T,S)
  writeFile(result)

