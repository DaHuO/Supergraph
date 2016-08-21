
def getDigits(n):
    return [int(x) for x in str(n)]

def solve(n):
    if (n == 0):
        return "INSOMNIA"
    digits = []
    mult = 1
    go = True
    while len(digits) < 10:
        for d in getDigits(n * mult):
            if not d in digits:
                digits.append(d)
        mult += 1
    if (len(digits) == 10):
        return (mult - 1) * n
    return "INSOMNIA"


def main():
    f = open("A-large.in", 'r')
    lines = f.readlines()
    f.close()

    outFile = open("out.txt", 'w')
    for i, n in enumerate(lines[1:]):
        out = "Case #"+str(i + 1)+": " + str(solve(int(n)))+"\n"
        outFile.write(str(out))


main()
