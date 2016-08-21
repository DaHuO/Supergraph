
# IO files
#inputfile = open("input.txt", "r")
#inputfile = open("A-small-attempt1.in", "r")
inputfile = open("A-large.in", "r")
outputfile = open("output.txt", "w")

# Test cases
line = inputfile.readline()
cases = int(line) + 1
line = inputfile.readline()

# Solve the cases
for i in range(1, cases):
    if i > 1:
        outputfile.write("\n")
    
    # Solve problem
    parties = int(line)
    line = inputfile.readline()
    if line[-1] != '\n':
        line += "\n"
    print(line, end="")
    persons = []
    total = 0
    for j in range(0, parties):
        index = line.find(" ")
        inpval = int(line[:index])
        persons.append(inpval)
        line = line[index+1:]
        total += persons[j]
    
    result = ""
    two = 0
    for j in range(1, total-1):
        maxval = 0
        value = 0
        for k in range(0, len(persons)):
            if maxval < persons[k]:
                maxval = persons[k]
                value = k
        two += 1
        if two%2 == 0:
            result += str(chr(65 + value)) + " "
        else:
            result += str(chr(65 + value))
        persons[value] -= 1
    if two%2 == 1:
        result += " "
    for k in range(0, len(persons)):
        if persons[k] > 0:
            result += str(chr(65 + k))
    
    outputfile.write("Case #" + str(i) + ": " + result)
    print(": " + result)
    line = inputfile.readline()

# Close files
outputfile.close()
inputfile.close()