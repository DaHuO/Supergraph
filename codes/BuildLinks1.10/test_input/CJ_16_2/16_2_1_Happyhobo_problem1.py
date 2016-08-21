def read_words(afile):
    words = []
    for line in afile:
        words.append(line.strip())
    return words

def isIN(herp, number): #number is the string of the number
    
    string = []
    for k in herp:
        string.append(k)
    for i in range(len(number)):
        isGood = False
        for j in range(len(string)):
            if(string[j] == number[i]):
                string[j] = " "
                number[i] = " "
                isGood = True
                break
        if(not isGood):
            return False
    return True


def remove(string, number):
    for i in range(len(string)):
        for j in range(len(number)):
            if(string[i] == number[j]):
                string[i] = " "
                number[j] = " "
                break
    return string



filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text


nums = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
for i in range(int(T)):
    fin = []
    string = list(aList[i])
    numChars = len(string)
    tryNum = 0
    while(numChars > 0):
       
        if(tryNum > 9):
            temp = fin.pop()
            
            for elt in nums[temp]:
                string.append(elt)
            tryNum = temp+1
            numChars += len(nums[temp])

        elif(isIN(string, list(nums[tryNum]))):
            string = remove(string, list(nums[tryNum]))
            numChars -= len(nums[tryNum])
            fin.append(tryNum)
            
        else:
            tryNum += 1
    print "Case #"+str(i+1)+":",
    derp = ""
    for j in range(len(fin)):
        derp += str(fin[j])
    print derp

    
