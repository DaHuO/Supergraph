x = open('A-Large.in')

y = x.read()
final = []
temp = ''
for i in range(len(y)):
    if y[i] == ' ' or y[i] == "\n":
        temp = int(temp)
        final.append(temp)
        temp = ''
    else:
        temp += y[i]
        if i == len(y)-1:
            final.append(int(temp))
        continue
print (final)

real = [0,1,2,3,4,5,6,7,8,9]
realcounter = 1
for i in final:
    count = 0
    tester = [12,12,12,12,12,12,12,12,12,12]
    teatime = i
    test = False
    if i == 0:
        print ("Case #" + str(realcounter) + ": INSOMNIA")
        realcounter += 1
        continue
    while test == False:
        temp = str(teatime)
        for letter in temp:
            tester[int(letter)] = int(letter)
        if tester == real:
            test = True
            print ("Case #" + str(realcounter) + ": " + str(teatime))
        count += 1
        teatime = i * (count+1)
    realcounter += 1
        
