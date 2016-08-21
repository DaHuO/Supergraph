digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def num(x):
    seen = set()
    for i in range(1, 100000):
        number = str(x * i)
        for d in number:
            seen.add(d)
        if seen == digits:
            return number
    if seen != digits:
        return "INSOMNIA"


with open("A-large.in", "r") as f:
    cases = int(f.readline())
    cont = 1
    for i in range(cases):
        print("Case #{0}: {1}".format(cont, num(int(f.readline()))))
        cont += 1
