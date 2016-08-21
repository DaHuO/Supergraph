import time

def count_sheep(a):
    if a == 0:
        return "INSOMNIA"
    digits = set([str(x) for x in range(10)])
    i = 1
    while(True):
        b = a * i
        for c in str(b):
            if c in digits:
                digits.remove(c)
            if len(digits) == 0:
                return b
        i += 1

f = open("input.txt", "r+")
lines = tuple(f)
print count_sheep(11)
with open("output.txt", "w+") as o:
    for i in range(1, len(lines)):

        o.write("Case #%d: %s\n" % (i, str(count_sheep(int(lines[i])))))

