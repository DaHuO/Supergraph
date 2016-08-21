__author__ = 'ben'

lines = [int(line.rstrip('\n')) for line in open('input')][1:]

outFile = open("output", "w")

c = 1
for line in lines:
    digitsSeen = []
    i = 1

    if line == 0:
        outFile.write("Case #{}: INSOMNIA\n".format(c))
        c += 1
        continue

    while len(digitsSeen) != 10:
        letters = list(str(line * i))
        for letter in letters:
            if letter not in digitsSeen:
                digitsSeen.append(letter)
        i += 1
    outFile.write("Case #{}: {}\n".format(c, line*(i-1)))
    c += 1
