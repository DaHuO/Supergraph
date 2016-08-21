def getVerdict(N):
    digits = set()
    for digit in str(N):
        digits.add(int(digit))

    if len(digits) == 10:
        return N

    previous = N
    i = 2
    while True:
        new_number = i * N

        if previous == new_number:
            return "INSOMNIA"

        for digit in str(new_number):
            digits.add(int(digit))

        if len(digits) == 10:
            return new_number

        i += 1


def main():
    cases = int(raw_input())
    for i in range(cases):
        result = getVerdict(int(raw_input()))
        print "Case #" + str((i + 1)) + ": " + str(result)
    return

if __name__ == "__main__":
    main()
