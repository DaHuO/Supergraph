
def returnList(n):
    n = str(n)
    digits = list(n)
    return digits

def check(all):
    stat = False
    for i in range(10):
        if str(i) in all:
            stat = True
        else:
            stat = False
            break
    return stat

testCases = int(raw_input())

for i in range(testCases):
    N = int(raw_input())
    if N == 0:
        print "Case #"+str(i+1)+": INSOMNIA"
    else:
        listOfNum = returnList(N)
        j=1
        while True:
            if check(listOfNum):
                print "Case #"+str(i+1)+": "+str(newNumber)
                break

            j = j+1
            newNumber = N*j
            listOfNum.extend(returnList(newNumber))
            listOfNum = list(set(listOfNum)) 
