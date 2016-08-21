import string

file = open("A-large.in", "r")
newFile = open("output.txt", "w")

def charPos(letter):
    return ord(letter) - 97

def findLastWord(s:str):
    word = s[0]
    pChar = s[0]
    s = s[1:]
    for i in s:
        if (charPos(i) > charPos(pChar) or charPos(i) == charPos(pChar)):
            word = i + word
            pChar = i
        elif (charPos(i) < charPos(pChar)):
            word += i
            pChar = word[0]
    return word
            
    

# REPLACE THE functionName TO THE FUNCTION
testCases = int(file.readline())
for i in range(testCases):
    s = "Case #{}: {}".format(i + 1, findLastWord(file.readline()))
    
    newFile.write(s)

file.close()
newFile.close()
