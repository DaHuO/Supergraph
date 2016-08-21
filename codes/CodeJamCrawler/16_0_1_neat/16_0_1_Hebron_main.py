f = open('A-large.in', "r")
o = open('output.txt', "w")
numCases = int(f.readline())
for case in range(1, numCases + 1):
    input = int(f.readline())
    if input == 0:
        # Print Insomnia
        o.write("Case #" + str(case) + ": INSOMNIA")
    else:
        dict = {'0':'0', '1':'0', '2':'0', '3':'0', '4':'0', '5':'0', '6':'0', '7':'0', '8':'0', '9':'0'}
        n = 1
        dictComplete = False
        while(not dictComplete):
            currentNum = n * input

            for i in range(0, len(str(currentNum))):
                dict.__setitem__(str(currentNum)[i], '1')
                dictComplete = all(value == '1' for value in dict.values())
                if dictComplete:
                    break
            n += 1

        o.write("Case #" + str(case) + ": " + str(currentNum))
    o.write("\n")

print "Done!"

o.close()