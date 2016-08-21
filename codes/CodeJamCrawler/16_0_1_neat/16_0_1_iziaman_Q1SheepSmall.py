


class Bleatrix(object):
    def __init__(self):
        self.startBleatrix()

    def getInput(self):
        rounds= int(input())
        inputs=list()
        for i in range(rounds):
            inputs.append(int(input()))
        return inputs

    def getInput(self,fileName):
        self.nums=list()
        f =open(fileName)
        lines=f.readlines()
        for i in range(len(lines)):
            lines[i]=int(lines[i])
        lines.pop(0)
        return lines


    def startBleatrix(self):
        self.round=0
        self.res=False
        self.numOfRounds=self.getInput("A-large.in")
        while self.round < len(self.numOfRounds):
            self.playRound(self.numOfRounds[self.round])
            self.round+=1

    def checkResualt(self):
        for i in self.nums:
            if i ==False:
                return False
        return True

    def checkEquRound(self,oldSet=list()):
        for i in range(len(oldSet)):
            if oldSet[i] != self.nums[i]:
                return False
        return True

    def createNums(self):
        self.nums=list()
        for i in range(10):
            self.nums.append(False)


    def playRound(self, n):
        tmp=n ; i=0 ; found=True
        self.createNums()
        oldNums=self.nums[:]
        while not self.checkResualt():
            i+=1
            self.setNums(tmp*i)

            if i % 1000 ==0:
                if self.checkEquRound(oldNums):
                    self.printRes("INSOMNIA")
                    found=False
                    break
                else:
                    oldNums=self.nums[:]

        if found:
            self.printRes(i*tmp)
    def setNums(self,i):
        while i>0:
            x=i %10
            self.nums[x]=True
            i=i//10

    def printRes(self, i):
        print("Case #{}: {}".format(self.round+1,i))


if __name__=="__main__":
    Bleatrix()
