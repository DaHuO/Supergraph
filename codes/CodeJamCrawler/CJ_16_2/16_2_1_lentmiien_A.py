
# IO files
#inputfile = open("input.in", "r")
#inputfile = open("A-small-attempt2.in", "r")
inputfile = open("A-large.in", "r")
outputfile = open("output.out", "w")

# Test cases
line = inputfile.readline()
cases = int(line) + 1
line = inputfile.readline()

# Solve the cases
for i in range(1, cases):
    if i > 1:
        outputfile.write("\n")
    if line[-1] == "\n":
        line = line[:-1]
    print(line, end="\n")

    # Load data
    # no extra data
    
    # Solve problem
    alphabet = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    used = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(0, len(line)):
        alphabet[ord(line[j]) - ord('E')] += 1
    for k in range(0, 10):
        if k == 0:
            number = alphabet[ord('Z') - ord('E')] - used[ord('Z') - ord('E')]
            used[ord('Z') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            used[ord('R') - ord('E')] += number
            used[ord('O') - ord('E')] += number
            numbers[0] = number
        if k == 1:
            number = alphabet[ord('W') - ord('E')] - used[ord('W') - ord('E')]
            used[ord('T') - ord('E')] += number
            used[ord('W') - ord('E')] += number
            used[ord('O') - ord('E')] += number
            numbers[2] = number
        if k == 2:
            number = alphabet[ord('U') - ord('E')] - used[ord('U') - ord('E')]
            used[ord('F') - ord('E')] += number
            used[ord('O') - ord('E')] += number
            used[ord('U') - ord('E')] += number
            used[ord('R') - ord('E')] += number
            numbers[4] = number
        if k == 3:
            number = alphabet[ord('X') - ord('E')] - used[ord('X') - ord('E')]
            used[ord('S') - ord('E')] += number
            used[ord('I') - ord('E')] += number
            used[ord('X') - ord('E')] += number
            numbers[6] = number
        if k == 4:
            number = alphabet[ord('G') - ord('E')] - used[ord('G') - ord('E')]
            used[ord('E') - ord('E')] += number
            used[ord('I') - ord('E')] += number
            used[ord('G') - ord('E')] += number
            used[ord('H') - ord('E')] += number
            used[ord('T') - ord('E')] += number
            numbers[8] = number
        if k == 5:
            number = alphabet[ord('O') - ord('E')] - used[ord('O') - ord('E')]
            used[ord('O') - ord('E')] += number
            used[ord('N') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            numbers[1] = number
        if k == 6:
            number = alphabet[ord('T') - ord('E')] - used[ord('T') - ord('E')]
            used[ord('T') - ord('E')] += number
            used[ord('H') - ord('E')] += number
            used[ord('R') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            numbers[3] = number
        if k == 7:
            number = alphabet[ord('F') - ord('E')] - used[ord('F') - ord('E')]
            used[ord('F') - ord('E')] += number
            used[ord('I') - ord('E')] += number
            used[ord('V') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            numbers[5] = number
        if k == 8:
            number = alphabet[ord('S') - ord('E')] - used[ord('S') - ord('E')]
            used[ord('S') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            used[ord('V') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            used[ord('N') - ord('E')] += number
            numbers[7] = number
        if k == 9:
            number = alphabet[ord('I') - ord('E')] - used[ord('I') - ord('E')]
            used[ord('N') - ord('E')] += number
            used[ord('I') - ord('E')] += number
            used[ord('N') - ord('E')] += number
            used[ord('E') - ord('E')] += number
            numbers[9] = number

    result = ""
    for l in range(0, 10):
        result += str(l)*numbers[l]
    
    # Save result
    outputfile.write("Case #" + str(i) + ": " + result)
#    print(": " + result)
    line = inputfile.readline()

# Close files
outputfile.close()
inputfile.close()
