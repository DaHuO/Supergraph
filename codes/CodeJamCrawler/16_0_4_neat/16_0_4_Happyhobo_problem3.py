def read_words(afile):
    words = []
    for line in afile:
        words.append(line.strip())
    return words


filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text

for i in range(int(T)):
    
    line = aList[i].split() # number
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])

    final = []

    curNum = 1
    for j in range(K):
        final.append(curNum)
        curNum += K**(C-1)

    print "Case #"+str(i+1)+": ",
    for derp in final:
        print derp,
    print ""
        


