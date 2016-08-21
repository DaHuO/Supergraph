fin = file("A-large.in", "rU")
fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip()

    n = int(line)

    if n == 0:
        result = "INSOMNIA"
    else:
        # Keep track of numbers seen
        #seenarr = {"0": false, "1": false, "2": false, "3": false, "4": false,
        #"5": false, "6": false, "7": false, "8": false, "9": false}
        seenset = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        loops = 1
        nstr = str(n)

        while 1:
            #Iterate through current number
            for lett in nstr:
                if lett in seenset:
                    seenset.remove(lett)

            if len(seenset) == 0:
                result = nstr
                break
            
            loops += 1
            nstr = str(n*loops)


    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
