
def removeDigit(data, digitStr):
    for i in digitStr:
        data.remove(i)

    return data

def encodeDigit(data):
    answer = []

    prevData = data[:]

    while True:
        data = prevData[:]
        # case zero
        try:
            if prevData.index('Z') >= 0:
                answer.append('0')
                # remove zero
                prevData = removeDigit(prevData, 'ZERO')
        except:pass
        # case two
        try:
            if prevData.index('W') >= 0:
                answer.append('2')
                prevData = removeDigit(prevData, 'TWO')
        except:pass
        # case four
        try:
            if prevData.index('U') >= 0:
                answer.append('4')
                prevData = removeDigit(prevData, 'FOUR')
        except:pass
     
        # case six
        try:
            if prevData.index('X') >= 0:
                answer.append('6')
                prevData = removeDigit(prevData, 'SIX')
        except:pass
        
        # case eight
        try:
            if prevData.index('G') >= 0:
                answer.append('8')
                prevData = removeDigit(prevData, 'EIGHT')
        except:pass
 
        if len(data) == len(prevData): break
        
    while True:
        data = prevData[:]
        
        # last check
        # case one
        try:
            if prevData.index('O') >= 0:
                answer.append('1')
                prevData = removeDigit(prevData, 'ONE')
                continue
        except: pass
        # case three
        try:
            if prevData.index('H') >= 0:
                answer.append('3')
                prevData = removeDigit(prevData, 'THREE')
                continue
        except:pass
        # case five
        try:
            if prevData.index('F') >= 0:
                answer.append('5')
                prevData = removeDigit(prevData, 'FIVE')
                continue
        except:pass
        # case seven
        try:
            if prevData.index('S') >= 0:
                answer.append('7')
                prevData = removeDigit(prevData, 'SEVEN')
                continue
        except:pass
        # case nine
        try:
            if prevData.index('N') >= 0:
                answer.append('9')
                prevData = removeDigit(prevData, 'NINE')
                continue
        except:pass

        if len(prevData) == len(data): break
        
    return ''.join(str(s) for s in sorted(answer))

inputFile = open ('A-large.in', 'r')
outputFile = open('output.txt', 'w')

line = int(inputFile.readline())
digit = ['Z', 'ONE', 'W', 'THREE', 'U', 'FIVE', 'X', 'SEVEN', 'G', 'NINE']
for i in range(line):
    data = list(inputFile.readline().replace('\n', ''))

    outputFile.write('Case #{0}: {1}\n'.format((i + 1), encodeDigit(data)))

    
inputFile.close()
outputFile.close()
                     
                     
    
