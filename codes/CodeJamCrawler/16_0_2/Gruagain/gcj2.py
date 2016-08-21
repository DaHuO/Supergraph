def main():
    file = open('B-large.in', 'r')
    fileOut = open('output.txt', 'w')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToList(file.readline())
        answer = solve(line[0])
        output = "Case #" + str(x + 1) + ": " + str(answer)
        print(output)
        fileOut.write(output + '\n')
    file.close()
    fileOut.close()


def solve(line):
    counter = 0
    while "-" in line:
        if line[0] == '+':
            line = flip(line, line.find('-'), '+')
        else:
            line = flip(line, line.find('+'), '-')
        counter = counter + 1
    return counter


def flip(line, index, flipChar):
    if index == -1:
        index = len(line)
    print(line)
    print(index)
    flipped = line[0:index]
    unflipped = line[index:]
    print(flipped)
    print(unflipped)
    if flipChar == '+':
        flipped = flipped.replace('+', '-')
    else:
        flipped = flipped.replace('-', '+')
    line = flipped + unflipped
    print(line)
    return line


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()

if __name__ == '__main__':
    main()


''' If top is + count until hit -, flip all plus
If top is - count until +, flip all '''
