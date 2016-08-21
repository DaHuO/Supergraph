file = open('A-large(1).in', 'r')
myList = file.readlines()
for count in range(len(myList)):
    myList[count] = myList[count].replace('\n', '')

inputs = int(myList[0])
myList.pop(0)

#myList[0] = myList[0].split()

#print(myList)

fout = open('output.out', 'w')
for count in range(inputs):
    item = myList[count]
    answer = []
    #print(item)
    item = list(item)
    while item.count('Z') > 0:
        answer.append(0)
        item.remove('Z')
        item.remove('E')
        item.remove('R')
        item.remove('O')
    while item.count('W') > 0:
        answer.append(2)
        item.remove('T')
        item.remove('W')
        item.remove('O')
    while item.count('U') > 0:
        answer.append(4)
        item.remove('F')
        item.remove('O')
        item.remove('U')
        item.remove('R')
    while item.count('O') > 0:
        answer.append(1)
        item.remove('O')
        item.remove('N')
        item.remove('E')
    while item.count('R') > 0:
        answer.append(3)
        item.remove('T')
        item.remove('H')
        item.remove('R')
        item.remove('E')
        item.remove('E')
    while item.count('F') > 0:
        answer.append(5)
        item.remove('F')
        item.remove('I')
        item.remove('V')
        item.remove('E')
    while item.count('X') > 0:
        answer.append(6)
        item.remove('S')
        item.remove('I')
        item.remove('X')
    while item.count('V') > 0:
        answer.append(7)
        item.remove('S')
        item.remove('E')
        item.remove('V')
        item.remove('E')
        item.remove('N')
    while item.count('G') > 0:
        answer.append(8)
        item.remove('E')
        item.remove('I')
        item.remove('G')
        item.remove('H')
        item.remove('T')
    while item.count('I') > 0:
        answer.append(9)
        item.remove('N')
        item.remove('I')
        item.remove('N')
        item.remove('E')
    #print(item)
    drop = ''
    for item in sorted(answer):
        drop = drop + str(item)
    #print(drop)
    output = 'Case #' + str(count+1) + ': ' + drop
    print(output)
    fout.write(output + '\n')
fout.close()
    
        
