import fileinput


def main():
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        N = line.split(" ")[0]
        J = line.split(" ")[1]

        print("Case #1:")

        mid = (int(N)-2) * "0"

        for i in range(0, int(J)):
            out = generateDivisors(int(N)-2, mid)
            mid = out.split(" ")[0]
            mid = mid[1:len(mid)-1]
            s = generateNumber(int(mid, 2))
            mid = "0" * (int(N)-2 - len(s)) + s
            print(out)


def generateDivisors(size, mid):
    divisors = []
    string = ""
    while len(divisors) < 9:

        string = "1" + mid + "1"
        for j in range(2, 11):
            d = primeCheck(int(string, j))
            if d is not None:
                divisors.append(str(d))
            else:
                s = generateNumber(int(mid, 2))
                mid = "0" * (size - len(s)) + s
                divisors = []
                break

    return string + " " + " ".join(divisors)


def primeCheck(number):
    count = 0
    for i in range(2, 502):
        count += 1
        if number == i:
            return None
        if number % i == 0:
            return i

    return None

def generateNumber(num):
    return str(bin(num + 1)[2:])

if __name__ == "__main__":
    main()