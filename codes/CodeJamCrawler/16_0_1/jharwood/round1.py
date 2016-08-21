

def update_results(inputList, inputResults):
    for num in range(0,10):
        if num in inputList:
            inputResults[num] = True
    return inputResults

out = []
testCaseNumber = int(input())
for tc in range(1,testCaseNumber+1): #off by one because google starts at 1
    n = int(input())

    results = []
    for num in range(0,10):
        results.append(False)

    digits = list(map(int,str(n)))
    results = update_results(digits, results)
    #print(digits)
    #print(results)

    m = 2
    max_loop = 20000
    s_loop = 0
    while(results.count(False) > 0):
        s_loop += 1
        if(s_loop >= max_loop):
            temp = "INSOMNIA"
            break
        temp = n * m
        m = m + 1
        digits = list(map(int,str(temp)))
        #print(digits)
        results = update_results(digits, results)
        #print(results)
    out.append("Case #"+str(tc)+": "+str(temp))

#print(n)
for string in out:
    print(string)
