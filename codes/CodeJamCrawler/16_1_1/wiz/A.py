rf = open('A-large.in', 'r')
wf = open('A-large.out', 'w')
contents = rf.read().splitlines()
lineTotalNum = contents.pop(0)

for lineCounter in range(int(lineTotalNum)):
    line = contents[lineCounter]
    lineArr = line.split(' ')
    inputValue = lineArr[0]
    
    resultArray = []
#    print(inputValue);
    for i in range(len(inputValue)):
        if i == 0:
            resultArray.append(inputValue[i])
        elif resultArray[0] <= inputValue[i]:
#            print("bef:",resultArray)
            resultArray.insert(0, inputValue[i])
            #print("aft:",resultArray)
        else:
            resultArray.append(inputValue[i])

         

    

    
        
    wf.write("Case #" + str(lineCounter + 1) + ": " + ''.join(resultArray) + "\n")

rf.close()
wf.close()
print("End")
