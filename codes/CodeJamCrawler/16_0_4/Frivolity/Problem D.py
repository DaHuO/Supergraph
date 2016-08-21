#
# For each C >= 2, divide the patterns into K segments.
#
# For an L to appear in the first segment, the first tile
# in the initial pattern must have been L (otherwise, the first
# segment would be entirely G's).  Likewise, for an L to be
# in the i-th segment, the i-th tile in the initial pattern must
# be an L.
#
# You can divide this segment further if C >= 3, and a similar reasoning
# applies.  For K, C, and a spot n, the spot n is lead if and only if
# for each digit in n, the tile corresponding to that digit in the initial
# pattern is lead.  (Assuming these are 0-based indices, but they aren't so
# that has to be shifted down.  The idea still stands, however.)

inputFile = open("D-small-attempt0.in")
outputFile = open("D-small-attempt0.out", "w")

i = 0

for line in inputFile:
    if i > 0:
        parsed_line = line[:-1].split(' ')
        k = int(parsed_line[0])
        c = int(parsed_line[1])
        s = int(parsed_line[2])

        if k - c >= s:
            outputFile.write("Case #" + str(i) + ": IMPOSSIBLE\n")
        elif k > 1:
            output = "Case #" + str(i) + ":"
            a = 0
            while a == 0 or a < k - c + 1:
                check = 0
                b = 0
                while b < c and b < k:
                    check *= k
                    check += (a + b)
                    b += 1
                output += " " + str(check + 1)
                a += 1
            outputFile.write(output + '\n')
        else:
            outputFile.write("Case #" + str(i) + ": 1\n")
    i += 1

inputFile.close()
outputFile.close()
