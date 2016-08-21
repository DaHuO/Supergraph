def main():
    file = open('A-large.in', 'r')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToIntList(file.readline())
        answer = solve(line[0])
        output = "Case #" + str(x + 1) + ": " + str(answer)
        print(output)


def solve(line):
    digitsToBeFound = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    counter = 0
    if line is 0:
        return "INSOMNIA"
    while len(digitsToBeFound) > 0 and counter < 101:
        counter = counter + 1
        cur = line * counter
        cur = str(cur)
        for x in cur:
            if int(x) in digitsToBeFound:
                digitsToBeFound.remove(int(x))
    if len(digitsToBeFound) > 0:
        return "INSOMNIA"
    return line * counter


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()

if __name__ == '__main__':
    main()
