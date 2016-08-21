def read_words(afile):
    words = []
    for line in afile:
        words.append(line.strip())
    return words

filename = open('Untitled2.txt', 'r')
T = filename.readline()
aList = read_words(filename)
y = 0



while y < int(T):
    input = aList[y]
    og =  int(input)
    bl = True
    ints = []
    if int(input) == 0:
        print "Case #" + str(y+1) + ": INSOMNIA"


    else:
        while bl:
            i = 0
            while i < len(input):


                if input[i] not in ints:

                    ints.append(input[i])

                i += 1


            if len(ints) == 10:
                bl = False
                print "Case #" + str(y+1) + ": " + str(input)
            input = str(int(input) + og)


    y += 1
