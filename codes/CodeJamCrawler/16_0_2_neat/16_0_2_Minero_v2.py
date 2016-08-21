import fileinput

def main():

    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        print("Case #" + str(i) + ": " + str(countChanges(line.replace("\n", ""))))


def countChanges(line):
    quant = 0
    last = line[0]
    for i in line:
        if i != last:
            quant += 1
            last = i
    if line[len(line)-1] == "-":
        quant += 1
    return quant


if __name__ == "__main__":
    main()