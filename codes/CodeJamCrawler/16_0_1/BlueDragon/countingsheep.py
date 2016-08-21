file = open("/home/aidan/Documents/codejam16/A-large.in")
outFile = open("/home/aidan/Documents/codejam16/countingsheep-large.out", "w")

file.readline()
allDigits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

for index, line in enumerate(file):
    if line == "0\n":
        outFile.write("Case #{}: INSOMNIA\n".format(index+1))
    else:
        digits = set()
        startNumber = line.strip()
        multiplier = 2
        for char in startNumber:
            digits.add(char)
        while digits != allDigits:
            number = str(int(startNumber)*multiplier)
            multiplier += 1
            for char in number:
                digits.add(char)
        outFile.write("Case #{}: {}\n".format(index+1, number))
