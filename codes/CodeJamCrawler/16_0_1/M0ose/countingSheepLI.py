T = int(input())
while T < 1 or T > 100:
    T = int(input("Enter a number that is greater than or equal to 1 and less than or equal to 100"))

x = 0
cases = list()
while x < T:
    N = int(input())
    while N < 0 or N > 1000000:
        N = int(input("Enter a number that is greater than or equal to 0 and less than or equal to 200"))
    cases.append(N)
    x += 1

def checkDict(Dict):
    p = 0
    x = 0
    if Dict[0] == True and Dict[1] == True and Dict[2] == True and Dict[3] == True and Dict[4] == True and Dict[5] == True and Dict[6] == True and Dict[7] == True and Dict[8] == True and Dict[9] == True:
        return True
    else:
        return False
    
answers = list()


for i in cases:
    booldict = {0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
    f = 1
    last = 1
    while checkDict(booldict) == False:
        if i == 0:
            answers.append("INSOMNIA")
            booldict[0] = True
            booldict[1] = True
            booldict[2] = True
            booldict[3] = True
            booldict[4] = True
            booldict[5] = True
            booldict[6] = True
            booldict[7] = True
            booldict[8] = True
            booldict[9] = True
        a = str(i*f)
        last = i * f
        b = list(a)
        c = list()
        for d in b:
            c.append(int(d))
        for e in c:
            booldict[e] = True
        f += 1
        
    if checkDict(booldict) == True:
        answers.append(last)

CASE = 1
for a in answers:
    if a != 0:
        print('Case #',CASE,': ' ,a,sep='')
        CASE+=1

    
        
        
    
    
