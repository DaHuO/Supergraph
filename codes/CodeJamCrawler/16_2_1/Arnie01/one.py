import sys

numlines = int(sys.stdin.readline())

numbers = (
    ("ZERO", 0),
    ("SIX", 6),
    ("SEVEN", 7),
    ("TWO", 2),
    ("EIGHT", 8),

    ("THREE", 3),
    ("FOUR", 4),
    ("FIVE", 5),



    ("NINE", 9),
    ("ONE", 1),
)

for line_num in range(numlines):
    phone_number = []
    line = list(sys.stdin.readline().strip())
    for number, digit in numbers:
        try_again = True
        while try_again:
            line_copy = line[:]
            for letter in number:
                if letter in line_copy:
                    del line_copy[line_copy.index(letter)]
                else:
                    try_again = False
                    break
            if try_again:
                line = line_copy
                phone_number.append(digit)
    print "Case #{}: {}".format(str(line_num + 1), "".join(str(i) for i in sorted(phone_number)))
