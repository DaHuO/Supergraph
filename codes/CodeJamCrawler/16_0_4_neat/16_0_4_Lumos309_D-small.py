# GCJ 2016 D-small

infile = open("D-small-attempt0.in", "r")
outfile = open("D-small-result.txt", "w")

T = int((infile.readline())[:-1])

for case in range(T):
    line = (infile.readline()).split(" ")
    string = ""
    for i in range(1, int(line[0]) + 1):
        string += str(i)
        string += " "
    outfile.write("Case #{0}: {1}\n".format(str(case + 1), string[:-1]))

infile.close()
outfile.close()
