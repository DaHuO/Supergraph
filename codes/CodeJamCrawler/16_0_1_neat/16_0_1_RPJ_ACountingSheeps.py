#https://code.google.com/codejam/contest/6254486/dashboard

def countSleepSheeps(n):
    if n==0:
        return 'INSOMNIA'
    cnt, digitLst = 0, set()
    while len(digitLst) != 10:
        cnt += 1
        digitLst |= set(str(n*cnt))
    return n*cnt

inputPath = r'C:\Users\Remi\Code\Data\A-large.in'
outputPath = r'C:\Users\Remi\Code\Data\A_large.out'
caseNb = None
outputFile = open(outputPath, 'w')
fct = countSleepSheeps
for i, line in enumerate(open(inputPath, 'r')):
    if not caseNb:
        caseNb = int(line)
        continue
    outputFile.write('Case #%s: %s\n' % (i, fct(int(line.strip()))))
outputFile.close()