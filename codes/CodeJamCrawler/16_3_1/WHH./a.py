infile = open("A-small-attempt0.in", "r")
outfile = open("A-small.out", "w")

t = int(infile.readline())
casenumber = 1
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(len(alphabet))
for x in range(t):
    n = int(infile.readline())

    plist = [0 for p in range(26)]

    count = 0
    
    temp = infile.readline()[:-1].split()
    print(temp)
    for i in range(len(temp)):
        plist[i] = int(temp[i])
        count += int(temp[i])

    print(plist)
    output = []
    while count:
        flag = True
        maximum = -1
        maximum2 = -1
        index = 0
        index2 = 0
        for i in range(len(plist)):
            if plist[i]>=maximum:
                maximum2 = maximum
                maximum = plist[i]
                index2 = index
                index = i
        
        if count!=3 and count!=1 and index!=index2:
            plist[index]-=1
            plist[index2]-=1
            count -=2
        elif count == 3 or count == 1:
            plist[index] -=1
            count-=1
            flag = False
        else:
            plist[index]-=2
            count-=2
        
        if flag:
            output.append(alphabet[index]+alphabet[index2])
        else:
            output.append(alphabet[index])
        print(output)
   
    print("Case #{}: ".format(casenumber), end='', file=outfile)
    for i in range(len(output)):
        print(output[i], end=' ', file=outfile)
    print('', file=outfile)
    casenumber+=1
        
print("done")
infile.close()
outfile.close()
