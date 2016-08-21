representation = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def decrease(num, hash):
    for ch in representation[num]:
        hash[ch] -= 1

for test in range(input()):
    print "Case #{}:".format(test+1),

    S = raw_input()

    count = {}

    numbers = [0] * 10

    for ch in S:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1


    if "Z" in count:
        for i in xrange(count["Z"]):
            numbers[0] += 1
            decrease(0, count)

    if "W" in count:
        for i in xrange(count["W"]):
            numbers[2] += 1
            decrease(2, count)

    if "U" in count:
        for i in xrange(count["U"]):
            numbers[4] += 1
            decrease(4, count)

    if "X" in count:
        for i in xrange(count["X"]):
            numbers[6] += 1
            decrease(6, count)


    if "G" in count:
        for i in xrange(count["G"]):
            numbers[8] += 1
            decrease(8, count)

    if "O" in count:
        for i in xrange(count["O"]):
            numbers[1] += 1
            decrease(1, count)

    if "T" in count:
        for i in xrange(count["T"]):
            numbers[3] += 1
            decrease(3, count)

    if "F" in count:
        for i in xrange(count["F"]):
            numbers[5] += 1
            decrease(5, count)

    if "I" in count:
        for i in xrange(count["I"]):
            numbers[9] += 1
            decrease(9, count)

    if "N" in count:
        for i in xrange(count["N"]):
            numbers[7] += 1

    result = ""
    for i in xrange(10):
        for j in xrange(numbers[i]):
            result += str(i)

    print result