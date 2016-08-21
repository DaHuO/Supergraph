from itertools import combinations
class Pancake(object):
    def __init__(self,filename):
        self.fileName=filename
        self.readInput()
        self.round=0
        #self.sets("++--")

        while self.round<len(self.lines):
            #c= self.getResualt(self.lines[self.round])
            c=self.checkAllFormation(self.lines[self.round])
            print(self.round,c)
            self.writeToOutput(c)
            self.round+=1

    def readInput(self):
        f =open(self.fileName+".in")
        self.lines=f.readlines()
        for i in range(len(self.lines)):
            self.lines[i]=self.lines[i][:len(self.lines[i])-1]
        f.close()
        self.numOfInput=int(self.lines[0])
        self.lines.pop(0)

    def sets(self,word):
        s=set(range(len(word)))
        subs=[set(j) for i in range(len(s)) for j in combinations(s,i+1)]
       # print(subs)
        return subs

    def writeToOutput(self,text):
        f=open(self.fileName+".out",'a+')
        f.write("Case #"+str(self.round+1)+": "+str(text)+"\n")
        f.close()

    def prepareMatrix(self, stkPank=str()):
        self.res=list()
        for i in range(len(stkPank)):
            x=list()
            for i in range(len(stkPank)):
                x.append(-1)
            self.res.append(x)
        print(self.res)

    def getResualt(self,stkPank=str(),i=0,count=0):
        print(self.round,stkPank,count,sep=',')
        if self.checkRes(stkPank):
            return count
        if i==len(stkPank):
            return -1
        res=list()
        x=self.getResualt(stkPank,i+1,count+1)
        if x>=0:
            res.append(x)
        stkPank=self.flip(stkPank,i+1)
        x=self.getResualt(stkPank,i+1,count+1)
        if x>=0:
            res.append(x)
        if len(res)>0:
            return min(res)
        else:
            return -1

    def checkRes(self,stkPank=str()):
        for i in stkPank:
            if i == '-':
                return False
        return True

    def checkAllFormation(self,word=str()):
        if self.checkRes(word):
            return 0
        subs=self.sets(word)
        res=list()
        for i in subs:
            tmp=word
            count=0
            for j in i:
                tmp=self.flip(tmp,j)
                count+=1
            if self.checkRes(tmp):
                res.append(count)
        if len(res)>0:
            return min(res)
        else:
            return -1


    def flip(self,stkPank=str(),i=0):
        res=""
        j=0
        while j<=i and j<len(stkPank):
            if(stkPank[j]=='-'):
                res+='+'
            else:
                res+='-'
            j+=1
        while j<len(stkPank):
            res+=stkPank[j]
            j+=1
        return res
Pancake("B-small-attempt1")