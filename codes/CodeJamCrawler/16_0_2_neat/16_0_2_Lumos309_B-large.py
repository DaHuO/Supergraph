# GCJ 2016 B-small

infile = open("B-large.in", "r")
outfile = open("B-large-result.txt", "w")

T = int(infile.readline()[:-1])

for case in range(T):
    stack = infile.readline()[:-1]
    flip = 0

    state = stack[0]
    for i in range(1, len(stack)):
        if stack[i] != state:
            state = stack[i]
            flip += 1
    if state == "-":
            flip += 1

    outfile.write("Case #{0}: {1}\n".format(str(case + 1), str(flip)))
            

infile.close()
outfile.close()
