import sys

sys.stdout = open("./ans.out", 'w')
def numberOfSheep(base):
    if base is 0:
        return "INSOMNIA"

    found_digits = set([])
    i = 1
    while (len(found_digits) < 10):
        product = base * i;
        found_digits = found_digits.union(set(str(product)))
        i += 1

    return str(product)

with open('input.in') as inp:
    for idx, line in enumerate(inp):
        if idx is 0:
            continue
        base = int(line)
        print "Case #%d: %s" %(idx, numberOfSheep(base))
