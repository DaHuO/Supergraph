#https://code.google.com/codejam/contest/6254486/dashboard

flenames = ["test","A-small-attempt0","A-large"]  #.in for input .out for output
flemask = [0,0,1]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

#           inR, inC, inW = [int(finp) for finp in flein.readline().split()]

            inN = int(flein.readline())

            if inN == 0:
                outstr = "Case #{}: INSOMNIA".format(ctrL + 1)
            else:

                digitsSeen = [False] * 10  # 0-9
                success = [True] * 10
                total = 0

                while digitsSeen != success:
                    total += 1
                    lastNum = inN * total
                    testN = lastNum

                    while testN > 0:
                        nextDigit = testN % 10
                        testN = testN // 10
                        digitsSeen[nextDigit] = True

#                    print inN * total, digitsSeen

                outpA = lastNum

                outstr = "Case #{}: {}".format(ctrL+1,outpA)

            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

