INPUT_FILE = r'D:\Downloads\FromChrome\B-large.in'
OUTPUT_FILE = INPUT_FILE.replace('.in', '.out')

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(x):
    normalized_x = ''
    last = None
    for s in x:
        if s not in ['-', '+']:
            continue
        if s != last:
            normalized_x += s
        last = s
    if len(normalized_x) == 0:
        raise Exception("Bad input")
    if normalized_x[-1] == '+':
        normalized_x = normalized_x[:-1]
    return str(len(normalized_x))

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    x = inputFile.readline()
    result = solveQuestion(x)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
#print file(OUTPUT_FILE, 'rb').read()

