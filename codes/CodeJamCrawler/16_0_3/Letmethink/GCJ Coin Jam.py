import math

def findFactor(n:int):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0

def convertToBinary(n:int):
    return int(bin(n)[2:])

def convertToBase(n:int, base:int):
    l = list(str(n))
    total = 0
    for i in range(len(l)):
        total += int(l[i])*int(math.pow(base,len(l)-1-i))
    return total

file = open('SampleData.in', 'r')
myList = file.readlines()
for count in range(len(myList)):
    myList[count] = myList[count].replace('\n', '')

#print(myList)

inputs = int(myList[0])
myList.pop(0)

myList[0] = myList[0].split()
#myList[0].pop(1)

print(myList)

power = int(myList[0][0])
toFind = int(myList[0][1])
found = 0

#print(power)
#print(toFind)

output = []

for number in range (int(math.pow(2, power-1)+1), int(math.pow(2, power)), 2):
    #print(number)
    binary = convertToBinary(number)
    l = [binary]
    #print(binary)
    for i in range(2,11):
        basic = convertToBase(binary, i)
        #print(basic)
        #print(findFactor(basic))
        l.append(findFactor(basic))
    if l.count(0) == 0:
        #print('found1')
        found += 1
        output.append(l)
        if found == toFind:
            #print('here')
            break

#print(output)
fout = open('output.out', 'w')
foutput = 'Case #1:'
print(foutput)
fout.write(foutput + '\n')

for item in output:
    for n in range(len(item)):
        item[n] = str(item[n])
    foutput = item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + ' ' + item[4] + ' ' + item[5] + ' ' + item[6] + ' ' + item[7] + ' ' + item[8] + ' ' + item[9]
    print(foutput)
    fout.write(foutput + '\n')
file.close()
fout.close()
'''
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
output = 'Case #' + str(count+1) + ':'
fout.write(output + '\n')
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
    output = 'Case #' + str(count+1) + ':'
    print(output)
    fout.write(output + '\n')
#file.close()
fout.close()
'''
