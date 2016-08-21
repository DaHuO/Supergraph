from itertools import tee, izip

importResults = list()

while True:
    try:
        text = raw_input()
        if len(text.strip()) == 0:
            break
        else:
            importResults.append(text.strip())
    except EOFError:
        break

def makeJamcoin(n, j):
    # only handles the case where n is even
    factor_string = str(10**(n/2) + 1)
    bases = range(2, 11)
    factors = map(lambda base: int(factor_string, base), bases)
    for i in xrange(j):
        format_string = '#0' + str(int(n/2)) + 'b'
        top_half = "1" + format(i, format_string)[2:] + "1"
        print top_half + top_half + " " + " ".join(map(str, factors))

for i in range(len(importResults)):
    if i == 0:
        pass # this corresponds to the number of items
    else:
        print "Case #1:"
        makeJamcoin(32, 500)



