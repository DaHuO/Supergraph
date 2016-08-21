fin = file("B-large.in", "rU")
fout = file("B-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip()

    if line[0] == "-":
        flipstate = False #false for sad, true for happy
    else:
        flipstate = True

    #Go through and compare
    flips = 0

    for j in xrange(0, len(line)-1):
        #compare prev to curr
        if line[j] != line[j+1]:
            #flip
            flipstate = False if flipstate == True else True
            flips += 1

    if flipstate == False:
        flips += 1

    result = flips

    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
