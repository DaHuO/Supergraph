def getDigit(x):
    digits = set()
    while (x):
        digits.add(x % 10)
        x //= 10
    return digits


def get(x):
    if x == 0:
        return "INSOMNIA"
    i = 1
    digits = set()
    while (True):
        digits |= getDigit(x * i)
        if len(digits) == 10:
            return x * i
        i += 1

output = open("data.out", "w")


with open("data.in") as f:
    count = int(f.readline())
    for i in range(count):
        x = int(f.readline())
        output.write("Case #" + str(i + 1) + ": " + str(get(x)) + "\n")
