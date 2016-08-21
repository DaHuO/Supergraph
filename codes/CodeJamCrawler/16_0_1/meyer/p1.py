import sys

infn, outfn = sys.argv[1], sys.argv[2]
with open(infn) as infile:
    t = int( infile.readline().strip() )
    Ns = [int(line.strip()) for line in infile.readlines()]

mustread = set("1 2 3 4 5 6 7 8 9 0".split())

outfile = open(outfn, 'w')

for casenum, n in enumerate(Ns, start=1):
    accumulated = []
    highest = None
    m = 1

    if n == 0:
        highest = "INSOMNIA"
    while n != 0 and set(accumulated) != mustread:
        current_num = n * m
        current_numerals = [numeral for numeral in str(current_num)]
        accumulated += list(set(current_numerals))
        highest = current_num
        m += 1
    outfile.write("Case #" + str(casenum) + ": " + str(highest))
    outfile.write("\n")

