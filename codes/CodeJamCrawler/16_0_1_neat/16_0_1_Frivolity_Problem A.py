def compute(n):
    if (n == 0):
        return "INSOMNIA"
    digits = ["0", "1", "2", "3", "4", "5", "6", "7" , "8", "9"]
    i = 0
    while len(digits) > 0:
        i += 1
        for d in str(i*n):
            if (d in digits):
                digits.remove(d)
    return str(i * n)

inputFile = open("A-large.in")
outputFile = open("A-large.out", "a")
i = 0
for line in inputFile:
    if (i > 0):
        outputFile.write("Case #" + str(i) + ": " + compute(int(line)) + "\n")
    i += 1
outputFile.flush()
