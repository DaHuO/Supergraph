def countSleepSheeps(number):
    if number == 0:
        return 'INSOMNIA'
    count, sheepLst = 0, set()
    while len(sheepLst) != 10:
        count += 1
        for x in set(str(count * number)):
            sheepLst.add(x)
    return number*count

inFile = r'S:\Programming\GCJ2016\A-large.in'
outFile = r'S:\Programming\GCJ2016\A-large.out'
tstCase = None
outputFile = open(outFile, 'w')
fct = countSleepSheeps
for i, line in enumerate(open(inFile, 'r')):
    if not tstCase:
        tstCase = int(line)
        continue
    outputFile.write('Case #%s: %s\n' % (i, fct(int(line.strip()))))
outputFile.close()