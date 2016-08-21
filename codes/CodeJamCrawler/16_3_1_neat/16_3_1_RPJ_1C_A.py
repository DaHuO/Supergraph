EX = 'A'
SAMPLE = 'sample'
SAMPLE = 'small-attempt0'
SAMPLE = 'large'

partyDict = dict(zip(range(26), list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
def evacuate(senators):
    evacuationPlan = []
    evacuateMemberLst = ''

    while True:
        firstPartySize = max(senators)
        firstPartyLst = [i for i, j in enumerate(senators) if j == firstPartySize]
        if firstPartySize == 0:
            return ' '.join(evacuationPlan)
        if len(firstPartyLst) % 2 != 0:
            evacuationPlan.append(partyDict[firstPartyLst[0]])
            senators[firstPartyLst[0]] = senators[firstPartyLst[0]] - 1
        else:
            evacuationPlan.append(''.join(map(lambda x: partyDict[x], firstPartyLst[:2])))
            senators[firstPartyLst[0]] = senators[firstPartyLst[0]] - 1
            senators[firstPartyLst[1]] = senators[firstPartyLst[1]] - 1

if __name__ == '__main__':
    inputNb, nbParties = None, None
    outputFile = open(r'Data\%s_%s.out' % (EX, SAMPLE), 'w')
    for i, line in enumerate(open(r'Data\%s-%s.in' % (EX, SAMPLE))):
        if not inputNb:
            inputNb = int(line)
            continue
        if not nbParties:
            nbParties = int(line)
            continue
        else:
            outputFile.write('Case #%s: %s\n' % (int(i/2), evacuate([int(i) for i in line.strip().split()])))
            nbParties = None
    outputFile.close()


if __name__ == '__maidn__':
    print(evacuate([60,55, 56, 37, 51, 49, 52, 62, 43, 66, 44, 53, 51, 55, 56, 56, 45, 52, 51]))
