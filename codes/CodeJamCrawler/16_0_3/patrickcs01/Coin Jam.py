#coding:utf-8
import itertools
def readFile():
    file=open('C-small-attempt0.in','r')
    N=[]
    J=[]
    T=file.readline()
    for x in xrange(0,int(T)): # number of testcase
        n,j=file.readline().split()
        N.append(n)
        J.append(j)
    file.close()
    return T,N,J
def predo(N):
    res=[]
    b_res=[]
    min=int(N)-1
    for x in itertools.count(2**min+1):
        if(x==2**int(N)):
            break
        if(not(x%2==0)):
            k= bin(x).split("0b")[1]
            print k
            res.append(x)
            b_res.append(int(k))
    return res,b_res
def checkP(num):
    for i in xrange(2,1000):
       if (num % i) == 0:
           return i
    else:
        return 0
def CJ(res,b_res,target):
    resultkey=[]
    resultvalue=[]
    cnt=0
    cnt_J=0
    tmp=[]
    for x in xrange(0,len(res)):
        flag=True #只要有一個base是prime就flase不給跑
        cnt=0
        tmp=[]
        print "x:",x," 2Value:",b_res[x],"value:",res[x]
        for numberbase in xrange(2,11): #base:2~10 transfer to calc
            print numberbase,"base",int(str(b_res[x]),numberbase)
            if(flag==False): break
            cp=int(str(b_res[x]),numberbase)
            k=checkP(cp)
            print "K:",k
            if(k==0):
                flag=False
            else:
                tmp.append(k)
                #print "NOW tmp:",tmp
                cnt+=1
                if(cnt==9):
                    cnt_J=cnt_J+1
                    resultkey.append(b_res[x])
                    resultvalue.append(tmp)
                    if(cnt_J==int(target)):
                        return resultkey,resultvalue

    return resultkey,resultvalue
def writeFile(T,resultkey,resultvalue):
    print T
    file=open('CJ_result.in','w')
    for x in xrange(0,int(T)):
        file.write("Case #{0}:\n".format(x+1))
        for i in xrange(0,len(resultkey)):
            file.write(str(resultkey[i])+" ")
            for y in xrange(0,len(resultvalue[i])):
                file.write(str(resultvalue[i][y])+" ")
            file.write("\n")



if __name__ == '__main__':
    T,N,J=readFile()
    res=[]  #10s
    b_res=[] #binary
    result=[]
    for x in xrange(0,len(N)):
        res,b_res=predo(N[x]) # number of2**N[x]
        resultkey,resultvalue=CJ(res,b_res,J[x])
        print resultkey
        print resultvalue
        writeFile(T,resultkey,resultvalue)