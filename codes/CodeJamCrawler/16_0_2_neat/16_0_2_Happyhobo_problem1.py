def read_words(afile):
    words = []
    for line in afile:
        words.append(line.strip())
    return words


filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text

for i in range(int(T)):
    count = 0
    line = aList[i] # string of dashes and pluses
    line = list(line)
    for j in range(len(line)-1, -1, -1):
        if(line[j] == '-'):
            count += 1
            for k in range(j):
                if(line[k] == "-"):
                    line[k] = "+"
                else:
                    line[k] = "-"
    print "Case #"+str(i+1)+": "+str(count)
    


