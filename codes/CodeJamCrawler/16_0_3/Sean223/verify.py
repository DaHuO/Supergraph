IN_FILE = "large.txt"

with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
assert(next(it).strip() == 'Case #1:')

jamcoins_found = []

for i in range(1, 501):
    message = "Jamcoin on line " + str(i)
    line = next(it).strip().split()

    if not len(line) == 10:
        print(message + " had the wrong number of divisors listed!")

    jamcoin = line[0]
    if jamcoin in jamcoins_found:
        print(message + " was a duplicate!!")
    jamcoins_found.append(jamcoin)

    if not jamcoin[0] == '1':
        print(message + " did not start with 1!")

    if not jamcoin[-1] == '1':
        print(message + " did not end with 1!")

    for digit in jamcoin:
        if digit not in ('0', '1'):
            print(message + " had a non-binary digit!")

    if not len(jamcoin) == 32:
        print(message + " did not have 32 digits!")

    for base in range(2, 11):
        proposed_divisor = int(line[base-1])
        jamcoin_in_base = int(jamcoin, base)
        if proposed_divisor == 1 or proposed_divisor == jamcoin_in_base:
            print(message + " had a trivial divisor listed for base " + str(base))

        if not jamcoin_in_base % proposed_divisor == 0:
            print(message + " did not have a correct divisor listed for base " + str(base))

if not len(jamcoins_found) == 500:
    print("Did not find 500 jamcoins!")
