def read_words(afile):
    words = []
    for line in afile:
        words.append(line.strip())
    return words


filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text

for i in range(int(T)):
    
    line = aList[i] # number
    numbers = []

    if(line == "0"):
        print "Case #"+str(i+1)+": INSOMNIA"

    else:
        curNum = int(line)

        strNum = str(curNum)
        for j in strNum:
            if j not in numbers:
                numbers.append(j)

        while len(numbers) < 10:
            curNum += int(line)

            strNum = str(curNum)
            for j in strNum:
                if j not in numbers:
                    numbers.append(j)

        print "Case #"+str(i+1)+": "+str(curNum)
        


