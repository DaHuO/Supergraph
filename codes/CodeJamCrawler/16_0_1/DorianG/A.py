__author__ = 'Pascal'


def not_all_digits(digits):
    return not ('0' in digits and
                '1' in digits and
                '2' in digits and
                '3' in digits and
                '4' in digits and
                '5' in digits and
                '6' in digits and
                '7' in digits and
                '8' in digits and
                '9' in digits)

out = open('result.txt', 'w')
with open('A-large.in') as f:
    i = 1
    f.readline()
    for line in f:
        n = int(line)
        c = n
        digits = {x for x in list(str(n))}
        print(digits)
        b = 0
        while not_all_digits(digits):
            c += n
            for x in list(str(c)):
                if x not in digits:
                    digits.add(x)
                    b = 0
            print(digits)
            b += 1
            if b > 100:
                c = "INSOMNIA"
                break
        out.write("Case #" + str(i) + ": " + str(c) + "\n")
        i += 1
out.close()
