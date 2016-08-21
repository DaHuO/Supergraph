

fileIn = "A-large.in"# "sheep-test"
fileOut = fileIn + "-out"


def is_solved(result):
    for r in result:
        if r == 0:
            return False
    return True


def add_numbers(result, value):
    v = value
    while value > 0:
        v = int(v/10)
        num = value - v*10
        result[num] = 1
        value = int(value/10)


def solve(n):
    if n == 0:
        return "INSOMNIA"

    i = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while not is_solved(result):
        i += 1
        add_numbers(result, n*i)
    return n*i


# OutPut function
def writeLine(i, value):
    fileout.write("Case #" + str(i) + ": " + str(value) + "\n")
    print "return value : " + str(value)


# Read the Input
file = open(fileIn, "r")
fileout = open(fileOut, "w")
index = 0
print "Starting the Algo"

for n in file.readlines():
    if index == 0:
        count = n
        index += 1

    else:
        value = solve(int(n))
        writeLine(index, value)
        index += 1

fileout.close();
file.close();


