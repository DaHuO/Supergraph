import sys
sys.stdout = open("output.txt", "w+")


def answer(N):
    digits = {}

    if N == 0:
        return "INSOMNIA"

    result = 0
    while len(digits) < 10:
        result += N
        for c in str(result):
            digits[c] = 1

    return result


for i in range(int(raw_input())):
    print "Case #%d: %s" % (i + 1, answer(int(raw_input())))
