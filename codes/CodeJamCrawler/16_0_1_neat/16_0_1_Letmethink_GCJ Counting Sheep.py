file = open('A-large.in', 'r')
myList = file.readlines()
for count in range(len(myList)):
    myList[count] = myList[count].replace('\n', '')

inputs = int(myList[0])

print(myList)
#inputs = 1
#myList = ['1', '1692']
fout = open('output.out', 'w')
for count in range(inputs):
    listed = myList[count+1]
    base = ''
    if int(listed) == 0:
        base = "INSOMNIA"
    else:
        listed = int(listed)
        total = listed
        iterations = 0
        usedList = [False, False, False, False, False, False, False, False, False, False]
        while usedList.count(False) != 0:
            myList2 = list(str(total))
            for item in myList2:
                usedList[int(item)-1] = True
            total += listed
            iterations += 1
        base = str(total-listed)
            

    output = 'Case #' + str(count+1) + ': ' + base
    print(output)
    fout.write(output + '\n')
#file.close()
fout.close()
