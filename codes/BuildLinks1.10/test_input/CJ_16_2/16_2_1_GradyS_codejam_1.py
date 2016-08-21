def readfile(filename):
    textfile = open(filename, 'r')
    text = ''
    while True:
        read = textfile.readline()
        if not read:
            break
        text += read
    return text

def writefile(filename, text):
    textfile = open(filename, 'w')
    textfile.write(text)
    textfile.close()

def count(val):
    digits = [False]*10
    total = 0
    while True:
        total += val
        for i in range(10):
            if str(i) in str(total):
                digits[i] = True
        if False not in digits:
            return total

def remove(case, string):
    case = case.lower()
    for char in string.lower():
        index = case.index(char)
        case = case[:index] + case[index+1:]
    return case.upper()

def digits(case):
    result = []
    while 'z' in case.lower(): # independent
        case = remove(case, 'zero')
        result.append(0)
    while 'w' in case.lower(): # independent
        case = remove(case, 'two')
        result.append(2)
    while 'u' in case.lower(): # independent
        case = remove(case, 'four')
        result.append(4)
    while 'x' in case.lower(): # independent
        case = remove(case, 'six')
        result.append(6)
    while 'g' in case.lower(): # independent
        case = remove(case, 'eight')
        result.append(8)
    while 'f' in case.lower(): # dependent on 4
        case = remove(case, 'five')
        result.append(5)
    while 'v' in case.lower(): # dependent on 5
        case = remove(case, 'seven')
        result.append(7)
    while 'r' in case.lower(): # dependent on 0, 4
        case = remove(case, 'three')
        result.append(3)
    while 'i' in case.lower(): # dependent on 5, 6, 8
        case = remove(case, 'nine')
        result.append(9)
    while 'o' in case.lower(): # dependent on 0, 2, 4
        case = remove(case, 'one')
        result.append(1)
    result.sort()
    return reduce(lambda x,y: x+y, [str(item) for item in result])

cases = [case for case in readfile("A-large.in").split("\n")[1:] if case != ""]
output = ""

for case in range(len(cases)):
    output += "Case #" + str(case+1) + ": " + digits(cases[case]) + ("\n" if case != len(cases)-1 else "")

writefile("output.txt", output)
