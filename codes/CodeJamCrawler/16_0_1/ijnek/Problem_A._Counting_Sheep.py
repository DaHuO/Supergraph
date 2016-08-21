file_object = open('A-large.in','r')
file_object2 = open('output.txt','w')

t = int(file_object.readline().rstrip('\n'))

for i in range(t):
    arrNumbers = [False for x in range(10)]
    number = int(file_object.readline().rstrip('\n'))
    originalNumber = number
    count = 1
    for j in str(number):
        arrNumbers[int(j)] = True
    while arrNumbers != [True for x in range(10)]:
        number = count * originalNumber
        for j in str(number):
            arrNumbers[int(j)] = True
        if count > 100:
            file_object2.write('Case #'+str(i+1)+': INSOMNIA\n')
            break
        count += 1
    if arrNumbers == [True for x in range(10)]:
        file_object2.write('Case #'+str(i+1)+': '+str(number)+'\n')



