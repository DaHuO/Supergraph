testnum = input()
trials = []
for x in range(testnum):
        trials.append(raw_input())
for x in range(testnum):
        N = trials[x]
        reverser = []
        for y in range(len(trials[x])):
                reverser.append(N[len(N)-y-1])
        counter = 0
        previous = "+"
        for y in range(len(N)):
                if reverser[y] != previous:
                        if previous == "+":
                                previous = "-"
                        else:
                                previous = "+"
                        counter += 1
        print "CASE #{0}: {1}".format(x+1, counter)
