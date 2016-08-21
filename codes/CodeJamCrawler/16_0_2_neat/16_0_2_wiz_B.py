rf = open('B-large.in', 'r')
wf = open('B-large.out', 'w')
contents = rf.read().splitlines()
lineTotalNum = contents.pop(0)
##print("lineTotalNum",lineTotalNum)
##print("contents:",contents);
for lineCounter in range(int(lineTotalNum)):
    line = contents[lineCounter]
    lineArr = line.split(' ')
    inputValue = lineArr[0]
    result = 0
    count = 0
    beforeChar = ''
##    print(inputValue)
    reverseValue = inputValue[::-1]
    for one in reverseValue:
        if count == 0 and one == '+':
            beforeChar = one
            count += 1
            continue

        if beforeChar != one:
            result += 1

        beforeChar = one
        count += 1

    wf.write("Case #" + str(lineCounter + 1) + ": " + str(result) + "\n")

rf.close()
wf.close()
print("End")
