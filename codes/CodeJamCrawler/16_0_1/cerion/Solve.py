inputData = [int(line.rstrip('\n')) for line in open('A-large.in', 'r')]
outputList = []

for i in range(1, inputData[0] + 1):
    seenNum = set()
    n = 1
    num = inputData[i]
    while True:
        if num == 0:
            outputList.append('Case #' + str(i) + ': INSOMNIA' + '\n')
            break

        multiplyedNum = num * n
        for d in str(multiplyedNum):
            seenNum.add(d)

        seenAsString = ''.join(str(x) for x in sorted(seenNum))
        if '0123456789' in seenAsString:
            outputList.append('Case #' + str(i) + ': ' + str(multiplyedNum) + '\n')
            break
        n += 1

with open("A-large.out", "w") as fw:
    fw.writelines(outputList)
