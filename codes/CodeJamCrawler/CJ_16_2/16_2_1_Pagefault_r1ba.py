INPUT_FILE = r'C:\Users\nativ\Downloads\FromChrome\A-large.in'
OUTPUT_FILE = INPUT_FILE.replace('.in', '.out')

inputFile = file(INPUT_FILE, 'rb')
numQuestions = int(inputFile.readline())
outputFile = file(OUTPUT_FILE, 'wb')

def solveQuestion(x):
    NUMBERS = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    NUMBERS_SET = [
            [
            ('Z', 'ZERO'),
            ('W', 'TWO'),
            ('U', 'FOUR'),
            ('X', 'SIX'),
            ('G', 'EIGHT') ],
            [
            ('O', 'ONE'),
            ('T', 'THREE'),
            ('F', 'FIVE'),
            ('S', 'SEVEN') ],
            [
            ('I', 'NINE') ] ]
    result = []
    for num_set in NUMBERS_SET:
        for unique_char, number in num_set:
            while unique_char in x:
                result.append(number)
                for l in number:
                    pos = x.find(l)
                    if -1 == pos:
                        raise Exception("Shit")
                    x = x[:pos] + x[pos+1:]
    if ([] == result) or len(x) > 0:
        raise Exception("Failed: %r" % x)
    phone = []
    for num in result:
        phone.append(NUMBERS.index(num))
    phone.sort()
    return ''.join(['%d' % x for x in phone])

for q in xrange(numQuestions):
    outputFile.write("Case #%d: " % (q+1))
    # Don't forget to read length of a list
    x = inputFile.readline().strip()
    result = solveQuestion(x)
    outputFile.write(result)
    outputFile.write("\n")

outputFile.close()
inputFile.close()
# print file(OUTPUT_FILE, 'rb').read()
