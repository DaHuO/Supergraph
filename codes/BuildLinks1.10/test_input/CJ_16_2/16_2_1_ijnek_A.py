file_object = open('A-large (3).in','r')
file_object2 = open('output.txt','w')

t = int(file_object.readline().rstrip('\n'))

for i in range(t):
    numbers = [0 for x in range(10)]
    line = list(file_object.readline().rstrip('\n'))
    phnNum = ""
    numbers[0] = line.count('Z')
    numbers[2] = line.count('W')
    numbers[6] = line.count('X')
    numbers[8] = line.count('G')
    numbers[7] = line.count('S')-numbers[6]
    numbers[5] = line.count('V')-numbers[7]
    numbers[4] = line.count('F')-numbers[5]
    numbers[3] = line.count('R')-numbers[4]-numbers[0]
    numbers[1] = line.count('O')-numbers[0]-numbers[2]-numbers[4]
    numbers[9] = int((line.count('N')-numbers[1]-numbers[7])/2)





    #x = int(file_object.readline().rstrip('\n'))   
    phnNum = ""
    for j in range(10):
        for _ in range(numbers[j]):
            phnNum += str(j)


    output = "Case #{}: {}\n".format(i+1,phnNum)
    file_object2.write(output)