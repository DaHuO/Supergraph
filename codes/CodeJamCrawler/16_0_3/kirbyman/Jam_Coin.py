import sys

def one_solution(N,J):
    res=""
    res2=list()
    i=0
    g=0
    tmp=""
    tmp1=tuple()
    tmp666=list()
    while(i<J and g<2**N):
        tmp2=True
        tmp3=list()
        tmp=génère_value(N,g)
        k=2
        while(k<=10 and tmp2):
            tmp1=ispremier(calcl_val(k,tmp))
            tmp3.append(tmp1[1])
            if tmp1[0]:
                tmp2=False
            k+=1
        if (tmp2 and not(tmp3 in tmp666)):
            tmp666.append(tmp3)
            i+=1
            res+=tmp
            for l in range(9):
                res+=" "+str(tmp3[l])
            res2.append(res)
            res=""
        g+=1
    return res2

def génère_value(N,i):
    return "1"+calc(N,i)+"1"

def calc(N,i):
    res=bin(i)[2:]
    size=len(res)
    for k in range(size,N-2):
        res='0'+res
    return res
        

def calcl_val(base,val):
    res=0
    size=len(val)
    for i in range(size):
        res+=int(val[size-1-i])*base**i
    return res
        
def ispremier(Value):
    res=0
    i=1
    j=0
    while(res==0 and i<Value-1 and j<=10000):
        i+=1
        if (Value%i==0):
            res+=1
        j+=1

    if res==0 or j>10000:
        return (True,i)
    else:
        return (False,i)
    
    
def Solution(file_name):
    stream=open(file_name,'r')
    read=((stream.readline()).split('\n'))[0]
    i=1
    res=list()
    read=stream.readline()
    read=read.split(' ')
    N=int(read[0])
    J=int(read[1])        
    print("Case #{}:".format(i))
    res=one_solution(N,J)
    for i in range(J):
        print(res[i])
        
        
        
if __name__=="__main__":
    Solution(sys.argv[1])
