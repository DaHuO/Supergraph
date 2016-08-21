def profile(unordered):
    ordered = sorted(unordered)
    letters = "abcdefghijklmnopqrstuvwxyz"
    profileDict = {}
    for i in letters.upper():
        profileDict[i] = unordered.count(i)
    return profileDict

def removeWord(dictionary, word, letter):
    wordCount = dictionary[letter]
    for i in word:
        dictionary[i] = dictionary[i] - wordCount
    return wordCount


def handleString(originalString):
    prof = profile(originalString)
    result = ""
    result+="6"*removeWord(prof,"SIX", "X")
    result+="7"*removeWord(prof,"SEVEN", "S")
    result+="0"*removeWord(prof,"ZERO", "Z")
    result+="4"*removeWord(prof,"FOUR", "U")
    result+="5"*removeWord(prof,"FIVE", "V")
    result+="2"*removeWord(prof,"TWO", "W")
    result+="8"*removeWord(prof,"EIGHT", "G")
    result+="9"*removeWord(prof,"NINE", "I")
    result+="3"*removeWord(prof,"THREE", "T")
    result+="1"*removeWord(prof,"ONE", "O")
    for i in prof:
        if prof[i]!=0:
            print originalString
    return "".join(sorted(result))
    

lines = open("phonein.txt").read().splitlines()
out = ""
for i in xrange(1, len(lines)):
    out+="Case #"+str(i)+": "+handleString(lines[i])+"\n"
open("phoneout.txt","w").write(out)


