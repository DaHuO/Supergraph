inputName = 'B-small-attempt0'

# Take input
infile = open(inputName + '.in', 'r')
lines = infile.readlines()
infile.close()

outfile = open(inputName + '-out.txt', 'w')

counter = 0
numTests = int(lines[counter])
testNum = 1
while testNum <= numTests:
    counter += 1

    N = int(lines[counter])

    # Build the rows
    rows = []
    for i in range(2*N-1):
        counter += 1
        rows.append([int(e) for e in lines[counter].strip().split()])

    # print(rows)
    result = []
    counts = {}

    # Find which numbers have an odd number of appearances
    # This tells you what numbers are in the row (there will be no duplicates)
    for x in range(N):
        for y in range(2*N-1):
            if rows[y][x] not in counts:
                counts[rows[y][x]] = 1
            else:
                counts[rows[y][x]] += 1

    # print(counts)

    rowPerm = []
    for key in counts:
        if counts[key] % 2 != 0:
            rowPerm.append(key)

    # row must be in strictly increasing order
    rowPerm.sort()
    # print(rowPerm)

    # Write output
    outfile.write('Case #' + str(testNum) + ': ' + ' '.join(str(e) for e in rowPerm))
    if testNum < numTests:
        outfile.write('\n')

    testNum += 1

outfile.close()
