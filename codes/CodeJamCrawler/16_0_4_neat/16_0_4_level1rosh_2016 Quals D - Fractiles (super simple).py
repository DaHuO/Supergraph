inputName = 'D-small-attempt3'

# Define gold = 1 and lead = 0

# Take input
infile = open(inputName + '.in', 'r')
lines = infile.readlines()
infile.close()

outfile = open(inputName + '-out.txt', 'w')

for x, line in enumerate(lines):
    if x == 0:
        numTests = int(line)
    else:
        seqLen, complexity, checkLimit = map(lambda y: int(y), line.split())

        if seqLen <= checkLimit:
            outfile.write('Case #' + str(x) + ': ' + ' '.join(str(x) for x in range(1, seqLen + 1)))
        else:
            outfile.write('Case #' + str(x) + ': ' + 'IMPOSSIBLE')

        if x < numTests:
            outfile.write('\n')

outfile.close()
