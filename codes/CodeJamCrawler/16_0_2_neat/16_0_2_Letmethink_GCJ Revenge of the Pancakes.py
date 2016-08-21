file = open('B-large.in', 'r')
myList = file.readlines()
for count in range(len(myList)):
    myList[count] = myList[count].replace('\n', '')

inputs = int(myList[0])
myList.pop(0)

tempList = []
for n in range(len(myList)):
    item = myList[n]
    tempList = list(item)
    tempList2 = tempList
    for i in range (len(tempList)):
        tempList2[i] = tempList[i] == '+'
    myList[n] = tempList2

#print(myList)          

fout = open('output.out', 'w')
for count in range(inputs):
    listed = myList[count]
    flips = 0
    while listed.count(False) != 0:
        #print(listed)
        flips += 1
        counter = 0
        valid = False
        while not valid:
            if counter == len(listed):
                valid = True
            elif listed[counter] != listed[0]:
                valid = True
            else:
                counter += 1
        #print(counter)
        #counter -= 1
        for iteration in range(counter):
            listed[iteration] = not listed[iteration]
    base = str(flips)
    output = 'Case #' + str(count+1) + ': ' + base
    print(output)
    fout.write(output + '\n')
#file.close()
fout.close()
