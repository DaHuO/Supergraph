import re

def checknum(num):
    if len(set(re.findall("\d",num)))==10:
        return True
    else:
        return False 

T = int(input())
N = [int(input()) for i in range(T)] 

for casenum in range(T):
    if N[casenum] == 0:
        print("Case #"+str(casenum+1)+": INSOMNIA")
    else:
        time = 1
        numall = ""
        while(True):
            number = N[casenum] * time
            numall = numall + str(number)
            #print(numall)
            if checknum(numall):
                break
            else:
                time = time + 1
                
        #Output
        print("Case #"+str(casenum+1)+": "+ str(number))
