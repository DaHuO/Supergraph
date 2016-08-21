FILENAME = "C-large"
INPUTFILE = FILENAME + ".in"
OUTPUTFILE = FILENAME + ".out"

inputfile = open(INPUTFILE, 'r')
outputfile = open(OUTPUTFILE, 'w')
NUMCASE = int(inputfile.readline())

content = inputfile.readline().split()
length = int(content[0])
howmany = int(content[1])
inputfile.close()


outputfile.write("Case #1:\n")

c = 0
num = 2 ** (length - 1)
while c < howmany:
    num_string = bin(num)[2:]
    if num_string[0] == '1' and num_string[-1] == '1':
        number = int(num_string)
        if (number % 11) == 0:
            c += 1
            print(c)
            print(num_string)
            outputfile.write(num_string)
            outputfile.write(" 3 4 5 6 7 8 9 10 11\n")
    num = num + 1

outputfile.close()