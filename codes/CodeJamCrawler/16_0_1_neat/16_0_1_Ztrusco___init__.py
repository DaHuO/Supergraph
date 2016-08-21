import fileinput

def main():
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            T = int(line.replace("\n", ""))
            continue
        a = insonia(int(line.replace("\n", "")))
        if a[1] >= 100:
            print("Case #" + str(i) + ": INSOMNIA")
        else:
            print("Case #" + str(i) + ": " + str(a[0]))


def insonia(e):
    vet = ""
    s = len(vet)
    i = 1
    string = ""
    while s < 10 and i < 100:
        string = str(e*i)
        for j in range(0, len(string)):
            b = vet.find(string[j])
            if b == -1:
                vet = str(vet + string[j])
            s = len(vet)
        i += 1
    return string, i

if __name__ == "__main__":
    main()