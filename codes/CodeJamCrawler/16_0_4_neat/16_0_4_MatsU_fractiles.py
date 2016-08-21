import math


def fractiles(inputfile, outputfile):
    fin = open(inputfile, "r")
    fout = open(outputfile, "w")
    no_of_cases = int(fin.readline())

    case_no = 1

    while case_no <= no_of_cases:
        k, c, s = fin.readline().strip("\n").split(' ')
        k = int(k)
        c = int(c)
        s = int(s)
        if s <= k - c:
            fout.write("Case #" + str(case_no) + ": IMPOSSIBLE\n")
        else:
            fout.write("Case #" + str(case_no) + ": ")
            next_tile = k
            while s > 1:
                fout.write(str(next_tile) + " ")
                next_tile -= 1
                s -= 1
            fout.write(str(next_tile) + "\n")

        case_no += 1

    fin.close()
    fout.close()

fractiles("sample.in", "sample.out")
fractiles("D-small-attempt0.in", "D-small-attempt0.out")