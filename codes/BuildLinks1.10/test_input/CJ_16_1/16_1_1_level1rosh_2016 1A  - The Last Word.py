inputName = 'A-large'

# Take input
infile = open(inputName + '.in', 'r')
lines = infile.readlines()
infile.close()

outfile = open(inputName + '-out.txt', 'w')

for x, line in enumerate(lines):
    if x == 0:
        numTests = int(line)
    else:
        result = []
        line=line.strip() # remove newline char
        result.append(line[0]) # add first char
        for i in range(1, len(line)):
            # if this letter comes before the first char in result, put it at the end
            if line[i] < result[0]:
                result.append(line[i])
            else:
                # This letter comes after result[0] in alphabet, so prepend
                result.insert(0, line[i])

        result = ''.join(result)
        # Write output
        outfile.write('Case #' + str(x) + ': ' + str(result))
        if x < numTests:
            outfile.write('\n')

outfile.close()
