f = open('input2.in', 'r')
t = int(f.readline().strip())
out = open('output2.txt', 'w')

def getUniqueVals(arr):
    answerArr = []
    current = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == current:
            count = count + 1
        else:
            if count % 2 == 1:
                answerArr.append(arr[i-1])
            current = arr[i]
            count = 1
    if count % 2 == 1:
        answerArr.append(arr[len(arr)-1])
    return answerArr

for i in range(t):
    n = int(f.readline())
    arr = []
    for j in range(2*n-1):
        inputStr = list(map(int, f.readline().strip().split(' ')))
        for val in inputStr:
            arr.append(val)
    arr.sort()
    #print (arr)
    vals = getUniqueVals(arr)
    vals.sort()
    vals = ' '.join(list(map(str, vals)))
    #print(vals)
    out.write("Case #" + str(i+1) + ": " + vals + "\n")
    
    
out.close()
f.close()


