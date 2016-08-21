import sys

def solve(number):
    digits_seen = []
    if number == "0":
        return 'INSOMNIA'

    i = 1
    while True:
        num = int(number) * i
        i = i + 1
        for digit in str(num):
            if digit not in digits_seen:
                digits_seen.append(digit)

            #print "Seen {} len {}".format(digits_seen, len(digits_seen))
            if len(digits_seen) == 10:
                return num

filename = 'input.txt'
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, 'r') as f:
    data = f.read()

    data = data.split("\n")
    data.pop(0)

    case = 0
    for line in data:
        if line == '': continue
        case = case + 1

        print "Case #{}: {}".format(case, solve(line))


