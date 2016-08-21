import fileinput

def digits(n):
    return [int(d) for d in list(str(n))]

def solve(n):
    if n == 0:
        return "INSOMNIA"

    number = n
    mult = 1
    count = 0
    table = [False] * 10
    while count < 10:
        number = n * mult
        mult += 1
        for d in digits(number):
            if not table[d]:
                table[d] = True
                count += 1
    return number

def main():
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        n = int(line)
        print("Case #{}: {}".format(i, solve(n)))

if __name__ == "__main__":
    main()
