testnum = input()
trials = []
for x in range(testnum):
        trials.append(input())
for x in range(testnum):
        N = trials[x]
        occurrence = []
        occurrencenum = []
        for y in range(1000):
                multiple = N*(y+1)
                numstring = str(multiple)
                for a in range(len(numstring)):
                        testvar = 0
                        for b in range(len(occurrence)):

                                if int(numstring[a]) == int(occurrence[b]):
                                        testvar = 1
                        if testvar != 1:
                                occurrence.append(int(numstring[a]))
                                occurrencenum.append(int(numstring))
                        if len(occurrence) == 10:
                                break
                if len(occurrence) == 10:
                        break
        if len(occurrence) == 10:
                print "Case #{0}: {1}".format(x+1, occurrencenum[len(occurrencenum)-1])
        else:
                print "Case #{0}: INSOMNIA".format(x+1)
