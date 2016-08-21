filename = "A-large"
fin = open(filename + ".in", "r")
fout = open(filename + ".out", "w")
casenum = int(fin.readline())
for ite in range(casenum):
    in_str = fin.readline()
    dignums = [0,0,0,0,0,0,0,0,0,0]
    dignums[0] = in_str.count('Z')
    dignums[2] = in_str.count('W')
    dignums[4] = in_str.count('U')
    dignums[6] = in_str.count('X')
    dignums[8] = in_str.count('G')
    dignums[3] = in_str.count('H') - dignums[8]
    dignums[5] = in_str.count('F') - dignums[4]
    dignums[1] = in_str.count('O') - dignums[0] - dignums[2] - dignums[4]
    dignums[7] = in_str.count('V') - dignums[5]
    dignums[9] = in_str.count('I') - dignums[5] - dignums[6] - dignums[8]
    return_str = ""
    for jte in range(10):
        return_str += str(jte) * dignums[jte]
    fout.write("Case #{0}: {1}\n".format(ite + 1, return_str))
