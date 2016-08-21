import pdb, sys

infn, outfn = sys.argv[1], sys.argv[2]

with open(infn) as infile:
    t = int( infile.readline().strip() )
    sequences = [[mark for mark in line.strip()] for line in infile.readlines()]

with open(outfn, 'w') as outfile:
    for casenum, seq in enumerate(sequences, start=1):
        contiguous = [seq.pop(0)]
        for mark in seq:
            if contiguous[-1] == mark:
                continue
            else:
                contiguous.append(mark)
        answer = None
        if contiguous[-1] == "-":
            answer = len(contiguous)
        elif contiguous[-1] == "+":
            answer = len(contiguous)-1

        outfile.write("Case #" + str(casenum) + ": " + str(answer))
        outfile.write("\n")
        

