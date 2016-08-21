class checkNumber:
    def __init__(self):
        self.numberDict={0:False,
                    1:False,
                    2:False,
                    3:False,
                    4:False,
                    5:False,
                    6:False,
                    7:False,
                    8:False,
                    9:False,
                    }
        self.counter=0
    def check(self,number):
        if "0" in number and self.numberDict[0] == False:
            self.numberDict[0]=True
            self.counter+=1
        if "1" in number and self.numberDict[1] == False:
            self.numberDict[1]=True
            self.counter+=1
        if "2" in number and self.numberDict[2] == False:
            self.numberDict[2]=True
            self.counter+=1
        if "3" in number and self.numberDict[3] == False:
            self.numberDict[3]=True
            self.counter+=1
        if "4" in number and self.numberDict[4] == False:
            self.numberDict[4]=True
            self.counter+=1
        if "5" in number and self.numberDict[5] == False:
            self.numberDict[5]=True
            self.counter+=1
        if "6" in number and self.numberDict[6] == False:
            self.numberDict[6]=True
            self.counter+=1
        if "7" in number and self.numberDict[7] == False:
            self.numberDict[7]=True
            self.counter+=1
        if "8" in number and self.numberDict[8] == False:
            self.numberDict[8]=True
            self.counter+=1
        if "9" in number and self.numberDict[9] == False:
            self.numberDict[9]=True
            self.counter+=1
        if self.counter == 10:
            return "exit"


def getNumber(number):
    counter=1
    checkNum=checkNumber()
    if number==0:
        return "INSOMNIA"
    while True:
        value=checkNum.check(str(number*counter))
        if value == "exit":
            return number*counter
        else:
            counter+=1


output_file=open("output.txt",'a')

with open("input.in") as input_file:
    counter=0
    totalInput=long(input_file.readline())
    for i in range(totalInput):
        value=getNumber(long(input_file.readline()))
        if i==totalInput-1:
            output_file.write("Case #{}: ".format(i+1)+str(value))
        else:
            output_file.write("Case #{}: ".format(i+1)+str(value)+"\n")
    
print "done"
output_file.close()