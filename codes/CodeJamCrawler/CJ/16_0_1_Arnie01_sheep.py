import itertools

handle = open("input.sheep.txt", "r")

for i in range(int(handle.readline())):
    number = int(handle.readline())
    if number == 0:
        print "CASE #{0}: INSOMNIA".format(i + 1)
    else:
        seen_digits = set()
        for multiplier in itertools.count(1):
            seen_digits.update(str(number * multiplier))
            if len(seen_digits) == 10:
                break
        print "CASE #{0}: {1}".format(i + 1, number * multiplier)