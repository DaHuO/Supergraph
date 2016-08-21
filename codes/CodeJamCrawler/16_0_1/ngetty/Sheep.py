def add_digits(number, digits):
    for d in number:
        digits.add(d)
    return digits

out = open("sheep-large.out", 'w')
file = "A-large.in"
with open(file, 'r') as infile:
    cases = infile.readlines()[1:]
    count = 0
    for case in cases:
        count += 1
        case = int(case)
        digits = set()
        n = 0
        if case != 0:
            while len(digits) < 10:
                n += 1
                number = case * n
                digits = add_digits(str(number), digits)
            print >> out, "Case #" + str(count) + ": " + str(number)
        else:
            print >> out, "Case #" + str(count) + ": INSOMNIA"