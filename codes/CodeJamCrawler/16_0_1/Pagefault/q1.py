INPUT_FILE = r"D:\downloads\fromchrome\A-large.in"
OUTPUT_FILE = INPUT_FILE.replace('.in', '.out')

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(x):
    current = [False] * 10
    for i in xrange(1, 0x10000):
        ix = i * x
        strx = str(ix)
        current = [current[d] or (str(d) in strx) for d in xrange(10)]
        if ([True] * 10) == current:
            return strx
    return 'INSOMNIA'

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    x = int(inputFile.readline())
    result = solveQuestion(x)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
