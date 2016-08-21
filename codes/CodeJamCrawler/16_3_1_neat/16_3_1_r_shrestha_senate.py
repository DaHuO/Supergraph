import sys

with open(sys.argv[1]) as f:
    content = f.read().splitlines()

def checkAllZero(a):
    for i in a:
        if i != 0:
            return False
    return True

with open('io/out.out', 'w') as f:
    T = int(content[0])
    for testIndex in range(T):
        partyNumbers = content[testIndex*2 + 2].split(' ')
        # convert to int
        partyNumbers = [int(i) for i in partyNumbers]
        originalPartyNumbers = [i for i in partyNumbers]
        plan = []
        maxProportion = []
        
        if sum(partyNumbers) % 2 != 0:
            maxParty = partyNumbers.index(max(partyNumbers))
            partyNumbers[maxParty] -= 1
            plan.append(chr(maxParty + ord('A')))
        # do while all senators evacuated
        while not checkAllZero(partyNumbers):
            tempPlan = ''

            maxParty = partyNumbers.index(max(partyNumbers))
            partyNumbers[maxParty] -= 1
            tempPlan += chr(maxParty + ord('A'))
            
            if not checkAllZero(partyNumbers):
                maxParty = partyNumbers.index(max(partyNumbers))
                partyNumbers[maxParty] -= 1
                tempPlan += chr(maxParty + ord('A'))
                
            if not checkAllZero(partyNumbers):
                maxProportion.append(float(max(partyNumbers)) / sum(partyNumbers))
            
            plan.append(tempPlan)
        
        planString = ' '.join(plan)
            
        
        f.write('Case #%d: %s\n' % (testIndex+1, planString))
        print 'Case #%d: %s' % (testIndex+1, planString)
        print originalPartyNumbers
        print maxProportion
        
        # debug
        # print '\rFinished Case %d' % (testIndex+1),
        
