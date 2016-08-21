file_object= open('B-large.in','r')
file_object2 = open('output.txt','w')

file_object.readline()
i=1
for line in file_object:
    line = line.rstrip('\n')
    arrLine = []
    count = 0
    for symbol in line:
        arrLine.append(symbol=='+') # + --> 1    
                                    # - --> 0
    for k in range(len(arrLine)-1):
        if arrLine[k] != arrLine[k+1]:
            count += 1
    if arrLine[-1] == 0:
        count += 1

    file_object2.write("Case #"+str(i)+": "+str(count)+'\n')
    i += 1