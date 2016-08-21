def pancakeRevenge(pancakes):
    cnt = sum(map(lambda i: pancakes[i] != pancakes[i+1], range(len(pancakes)-1)))
    return cnt + (pancakes[0]=='-' and (cnt%2)==0) + (pancakes[0]=='+' and (cnt%2)==1)

inputPath = r'C:\Users\Remi\Code\Data\B-large.in'
outputPath = r'C:\Users\Remi\Code\Data\B_large.out'
caseNb = None
outputFile = open(outputPath, 'w')
fct = pancakeRevenge
for i, line in enumerate(open(inputPath, 'r')):
    if not caseNb:
        caseNb = int(line)
        continue
    outputFile.write('Case #%s: %s\n' % (i, fct(line.strip())))
outputFile.close()