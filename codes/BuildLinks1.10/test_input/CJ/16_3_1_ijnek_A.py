file_object = open('A-large (4).in','r')
file_object2 = open('output.txt','w')

t = int(file_object.readline().rstrip('\n'))

for i in range(t):
    n = int(file_object.readline().rstrip('\n'))
    list = [int(x) for x in file_object.readline().rstrip('\n').split()]

    seq = ""

    while sum(list) != 2:

        stillHouses = []
        for house in range(len(list)):
            if list[house] != 0:
                stillHouses.append(house)
        if len(stillHouses) == 2:
            seq += chr(stillHouses[0]+65)+chr(stillHouses[1]+65)+' '
            list[stillHouses[0]]-=1
            list[stillHouses[1]]-=1
        else:
            biggestHouse = list.index(max(list))
            seq += chr(biggestHouse+65)+' '
            list[biggestHouse]-=1



    for j in range(len(list)):
        if list[j] == 1:
            seq += chr(j+65)


    output = "Case #{}: {}\n".format(i+1,seq)
    file_object2.write(output)