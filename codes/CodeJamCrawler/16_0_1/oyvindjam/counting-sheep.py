import sys

test_cases = sys.stdin.readline()

f = open("output", "w")

for test_case, number in enumerate(sys.stdin, 1):
    seenNumbers = []
    N = int(number)

    if (N == 0):
        f.write("Case #%d: %s\n" % (test_case, "INSOMNIA"))
    else:
        i = 1

        while True:
            digits_in_n = list(str(N * i))

            for digit in digits_in_n:
                if not digit in seenNumbers:
                    seenNumbers.append(digit)

            if len(seenNumbers) == 10:
                break

            i = i + 1

        f.write("Case #%d: %s\n" % (test_case, str(N * i)))
