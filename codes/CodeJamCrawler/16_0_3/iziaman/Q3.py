import string
import itertools
import random
import math
class JakovCoin(object):
    def __init__(self,n=6,j=3):

        self.candiate=self.genrateAllCandiateNumbers(n)
        self.j=j
        self.ans=self.checkAllNumsInBases()
        #self.j=len(self.ans)
        self.printRes(self.ans)

    def printRes(self,x):
        print ("Case #1:")
        i=0
        for v in x:
            if i<self.j:
                print(v, end=" ")
                tmp=x[v]
                t=0
                while t<len(tmp):
                    print(tmp[t],end=" ")
                    t+=1
            i+=1
            print()


    def checkAllNumsInBases(self):
        canidate=set()
        notCanidatet=set()
        ans=dict()
        k=0
        while k<len(self.candiate) and len(ans)<self.j:
            i=self.candiate[k]
            k+=1
            l=list()
            flag=False
            j=2
            while j<11 and not flag:
                x=self.bin2baseN(i,j)
                t=self.isPrime(x)
                l.append(t)
                if  t != -1:
                    canidate.add(i)
                else:
                    flag=True
                    notCanidatet.add(i)
                j+=1
            if not flag:ans[i]=l[:]
        '''
        tmp=canidate.difference(notCanidatet)
        for i in notCanidatet:
            del(ans[i])
        '''
        return ans

    def writeAllPrehmtive(self,str):
        f=open("prehamtive.out",'a+')
        f.write("Case #"+str(self.round+1)+": "+str+"\n")
        f.close()


    def genrateAllCandiateNumbers(self,n):
        res=list()
        num=list()
        temp=list()
        temp=["".join(seq) for seq in itertools.product("01", repeat=n-2)]
        #print(temp)
        i=0
        while i<len(temp):
            '''
            if i[0]=="1" and i[-1]=="1":
                res.append(i)
            '''
            temp[i]="1"+temp[i]+"1"
            i+=1
        print(temp)
        return temp

    def bin2baseN(self,num=str(),base=10):
        res=0
        i=0
        while i<len(num):
            res+=int(num[i])*(base**(len(num)-i-1))
            i+=1
        return res


    def baseN(self,num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
        return ((num == 0) and numerals[0]) or (self.baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

    def isPrime(self,n):
        if n<2: return -1
        i=2
        a=list()
        while i*i<=n:
            if n%i==0:
                return i
            i+=1
        return -1

    def test(self,str):
        for i in range(2,11):
            x=self.bin2baseN(str,i)
            print (x,end=" ")
            print (self.isPrime(x))

JakovCoin(32,500)