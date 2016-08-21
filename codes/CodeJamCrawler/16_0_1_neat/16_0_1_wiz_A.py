rf = open('A-large.in', 'r')
wf = open('A-large.out', 'w')
contents = rf.read().splitlines()
lineTotalNum = contents.pop(0)
##print("lineTotalNum",lineTotalNum)
##print("contents:",contents);
for lineCounter in range(int(lineTotalNum)):
    line = contents[lineCounter]
    lineArr = line.split(' ')
    inputValue = lineArr[0]
    result = "INSOMNIA"

    checkValue = inputValue
##    print("current inputValue:",inputValue)
    checkValueArr = [checkValue]
    storeArr = []
    while True:
        storeArr = sorted(set(storeArr + sorted(set(list(checkValue)))))
##        print(storeArr)
##        print("current inputValue:",inputValue)
        if ['0','1','2','3','4','5','6','7','8','9'] ==  storeArr:
##            print("End checkValue:",checkValue)
            result = checkValue
            break
        else :
##            print("storeArr:",storeArr);
            checkValue = str(int(checkValue) + int(inputValue))
##            print("added checkValue:",checkValue);
            if checkValue in checkValueArr:
                result = "INSOMNIA"
                break
            else:
                checkValueArr = sorted(set(checkValueArr + [checkValue]))


        
    wf.write("Case #" + str(lineCounter + 1) + ": " + str(result) + "\n")

rf.close()
wf.close()
print("End")
