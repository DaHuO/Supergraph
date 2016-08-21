

def getLastWord(word):
    max = None
    result = None
    for letter in word:
        if max == None:
            max = ord(letter)
            result = letter
            #print result
            continue
        if ord(letter) >= max:
            max = ord(letter)
            result = "%s%s" % (letter, result)
            # print result
        else:
            result = "%s%s" % (result, letter)
    return result


inFile = r'S:\Programming\GCJ2016\A-large.in'
outFile = r'S:\Programming\GCJ2016\A-large.out'
tstCase = None
outputFile = open(outFile, 'w')
fct = getLastWord
for i, line in enumerate(open(inFile, 'r')):
    if not tstCase:
        tstCase = int(line)
        continue
    outputFile.write('Case #%s: %s\n' % (i, fct(line.strip())))
outputFile.close()