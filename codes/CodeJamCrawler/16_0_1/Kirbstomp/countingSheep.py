input = open("A-large.in","r+")
cases = int(input.readline())
solution = open("solve.txt","w")
caseNum = 1
numList = [False]*10
print(numList)

def check_and_add(n,x):
    if (n == 0):
        return "INSOMNIA"
    for i in str(n*x):
        numList[int(i)] = True

    if all(numList):
        return n*x
    else:
        return check_and_add(n,x+1)

for x in range(0,cases):
    number = int(input.readline())
    ans = check_and_add(int(number),1)
    solution.write("Case #"+str(caseNum)+": "+str(ans)+"\n")
    caseNum +=1
    numList = [False]*10

