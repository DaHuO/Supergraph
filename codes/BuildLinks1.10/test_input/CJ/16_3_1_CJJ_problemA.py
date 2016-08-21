#Snate Evacuation
import sys

def readInput (filename):
    cases = []
    with open (filename, 'r') as file:
        numberOfCases = int(file.readline())
        for i in range(numberOfCases):
            parties = int(file.readline().replace('\n', ''))
            senators = [int(x) for x in file.readline().replace('\n', '').split(' ')]
            cases.append(senators)
    return numberOfCases, cases

def writeOutput (filename, output, numberOfCases):
    with open (filename, 'w') as file:
        for i in range(numberOfCases):
            line = "Case #" + str(i+1) + ": "
            line +=  output[i]
            line += '\n'
            file.write(line)

def problem (inputfile=".input", outputfile="output"):
    numberOfCases, cases = readInput(inputfile)
    output = []
    for case in cases:
        output.append(evacuationPlan(case))
    writeOutput(outputfile, output, numberOfCases)

PARTIES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def evacuationPlan (senators):
    plan = ''
    fstInd = senators.index(max(senators))
    auxsenators = senators[:fstInd] + senators[fstInd+1:]
    scdInd =  auxsenators.index(max(auxsenators))
    if scdInd >= fstInd:
        scdInd += 1
    plan += removeParty(PARTIES[fstInd], senators[fstInd]-senators[scdInd])
    for partyInd in range(len(senators)):
        if partyInd != fstInd and partyInd != scdInd:
            plan += removeParty(PARTIES[partyInd], senators[partyInd])
    plan += (PARTIES[fstInd]+PARTIES[scdInd]+' ')*senators[scdInd]
    return plan

def removeParty (party, nMembers):
    partyPlan = (party*2+' ')*(nMembers//2) + (party+' ')*(nMembers&1)
    return (partyPlan)

if __name__ == "__main__":
    problem(sys.argv[1])
