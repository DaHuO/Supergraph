import sys

cases = int(sys.stdin.readline())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(cases):
    nrofparties = int(sys.stdin.readline())
    parties = list(map(int, sys.stdin.readline().split(" ")))
    line = "Case #" + str(i+1) + ": "
    while max(parties) > 0:
        test = [value for value in parties if value != 0]
        if max(parties) == 1 and len(test) == 3:
            suurim = parties.index(max(parties))
            line += alphabet[suurim]
            parties[suurim] -= 1
            line += " "
        else:
            suurim = parties.index(max(parties))
            line += alphabet[suurim]
            parties[suurim] -= 1
            suurim = parties.index(max(parties))
            line += alphabet[suurim]
            parties[suurim] -= 1
            line += " "
    if line[-1] == " ":
        line = line[:-1]
    print(line)