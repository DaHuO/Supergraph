import sys

print 'Number of arg:', len(sys.argv)

f = open(sys.argv[1], 'r')
p = open(sys.argv[2], 'w')

noInput = f.readline()
caseNr = 0

for line in f:
    caseNr = caseNr + 1
    match = [0,1,2,3,4,5,6,7,8,9]
	
    line = int(line)
    workingLine = line
	
    while match:
        for a in list(str(workingLine)):
            if int(a) in match:
                match.remove(int(a))

        workingLine = workingLine + line

        if (workingLine+line) == line:
            workingLine = "INSOMNIA"
            match = []

    if not workingLine == "INSOMNIA":
        workingLine = workingLine-line

    print 'Case #%i: %s' %(caseNr, workingLine)
    p.write('Case #%i: %s\n' % (caseNr, workingLine))