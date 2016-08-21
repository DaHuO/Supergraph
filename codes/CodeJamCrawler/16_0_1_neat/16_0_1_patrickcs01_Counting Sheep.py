def readFile(fileName):
    file=open(fileName,'r')
    firstLine=file.readline()
    List=[int(x) for x in file.readlines()]
    file.close()
    return  firstLine,List
def P(T,List):
    result=[]
    for tetsIndex in range(0,int(T)):
        if (List[tetsIndex]==0):
            result.append('INSOMNIA')
        else:
            N=1
            cnt=0
            s=set()
            while N<=200:
                tmp= List[tetsIndex]
                dig=toDigits(tmp*N)
                for x in dig:
                    if x not in s:
                        s.add(x)
                        cnt+=1
                if(cnt==10):
                    result.append(tmp*N)
                    break
                else:
                    N=N+1
    return result
def toDigits(num):
    return [] if num == 0 else ([num % 10] + toDigits(num // 10))

def writeFile(result):
    file=open('result','w')
    for x in range(0,len(result)):
        file.write("Case #{0}: {1} \n".format(str(x+1), result[x]))
    file.close()
if __name__ == '__main__':
    firstLine,List=readFile('A-small-attempt1.in')
    result= P(firstLine,List)
    writeFile(result)