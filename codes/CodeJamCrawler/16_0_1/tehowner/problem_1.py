import logging


def add_num_to_set(seen, number):
    numbers = list(str(number))
    for number in numbers:
        seen[number] = 1


with open('A-large.in') as inpF:
    cases = int(inpF.readline())
    results = []
    for i in range(cases):
        print "new start number"
        startNumber = long(inpF.readline())
        print startNumber
        seenNumbers = {}

        add_num_to_set(seenNumbers, startNumber)
        if startNumber == 0:
            results.append("INSOMNIA")
            continue

        iteration = 2
        tmpNumber = 0
        while len(seenNumbers) < 10:
            tmpNumber = startNumber * iteration
            iteration += 1
            add_num_to_set(seenNumbers, tmpNumber)

            if iteration > 1000:
                break

        if iteration > 10000:
            results.append("INSOMNIA")
            continue

        results.append(str(tmpNumber))

    with open('o1', 'w+') as outF:
        for result in range(len(results)):
            outF.write("Case #{0}: {1}\n".format(result + 1, results[result]))
