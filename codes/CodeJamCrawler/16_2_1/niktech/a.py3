import sys
test_cases = open(sys.argv[1], 'r')

i = 1;
first = True
for test in test_cases:
    if (first):
        first = False
        continue
    line = test.replace('\n', '').replace('\r', '')

    # find zero
    result = [];
    index = line.find("Z")
    while index != -1:
        result.append("0");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("O");
        line = line[:index] + line[(index+1):]
        index = line.find("R");
        line = line[:index] + line[(index+1):]
        index = line.find("Z")

    # TWO
    index = line.find("W")
    while index != -1:
        result.append("2")
        line = line[:index] + line[(index+1):]
        index = line.find("O");
        line = line[:index] + line[(index+1):]
        index = line.find("T");
        line = line[:index] + line[(index+1):]
        index = line.find("W")

    # four
    index = line.find("U")
    while index  != -1:
        result.append("4");
        line = line[:index] + line[(index+1):]
        index = line.find("F");
        line = line[:index] + line[(index+1):]
        index = line.find("R");
        line = line[:index] + line[(index+1):]
        index = line.find("O");
        line = line[:index] + line[(index+1):]
        index = line.find("U")


    # six
    index = line.find("X")
    while index  != -1:
        result.append("6");
        line = line[:index] + line[(index+1):]
        index = line.find("I");
        line = line[:index] + line[(index+1):]
        index = line.find("S");
        line = line[:index] + line[(index+1):]
        index = line.find("X")

    # seven
    index = line.find("S")
    while index != -1:
        result.append("7");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("V");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("N");
        line = line[:index] + line[(index+1):]
        index = line.find("S")


    # Five
    index = line.find("F")
    while index  != -1:
        result.append("5");
        line = line[:index] + line[(index+1):]
        index = line.find("I");
        line = line[:index] + line[(index+1):]
        index = line.find("V");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("F")


    #one
    index = line.find("O")
    while index != -1:
        result.append("1");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("N");
        line = line[:index] + line[(index+1):]
        index = line.find("O")


    #three
    index = line.find("R")
    while index != -1:
        result.append("3");
        line = line[:index] + line[(index+1):]
        index = line.find("T");
        line = line[:index] + line[(index+1):]
        index = line.find("H");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("R")


    #nine
    index = line.find("N")
    while index  != -1:
        result.append("9");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("I");
        line = line[:index] + line[(index+1):]
        index = line.find("N");
        line = line[:index] + line[(index+1):]
        index = line.find("N")


    #eight
    index = line.find("I")
    while index  != -1:
        result.append("8");
        line = line[:index] + line[(index+1):]
        index = line.find("E");
        line = line[:index] + line[(index+1):]
        index = line.find("G");
        line = line[:index] + line[(index+1):]
        index = line.find("H");
        line = line[:index] + line[(index+1):]
        index = line.find("T");
        line = line[:index] + line[(index+1):]
        index = line.find("I")

    result.sort()
    t = ''.join(result)
    print("Case #" + str(i) + ": " + t);
    i+=1;
test_cases.close()