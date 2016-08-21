
import sys
import itertools

def formatOutput(n, result):
    return 'Case #' +  str(n) + ': ' + result + '\n'

file = open(sys.argv[1])
output = open('output.txt', 'w')
nTests = int(file.readline())

testNb = 1
for line in itertools.islice(file, 0, nTests+1):     
    k, c, s = (int(x) for x in line.split())
    answer = ''
    for x in range(1, k+1):
        answer += str(x) + ' '

    output.write(formatOutput(testNb, answer))
    testNb += 1
