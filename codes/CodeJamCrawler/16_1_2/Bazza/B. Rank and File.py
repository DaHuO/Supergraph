#https://code.google.com/codejam/contest/4304486/dashboard#s=p1

flenames = ["test","B-small-attempt0","B-large"]  #.in for input .out for output
flemask = [0,0,1]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

            inN = int(flein.readline())

            rowscols = []
            for ctrN in range(inN * 2 - 1):
               rowscols += ([int(finp) for finp in flein.readline().split()])

            rowscols.sort()
            print rowscols

            idx = 0
            while idx < len(rowscols) - 1:
                if rowscols[idx] == rowscols[idx+1]:
                    rowscols = rowscols[:idx] + rowscols[idx+2:]
                else:
                    idx += 1
#               print rowscols, idx

            outpA = ""
            for num in rowscols:
                outpA += str(num) + " "

            outstr = "Case #{}: {}".format(ctrL+1,outpA)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

