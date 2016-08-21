import os


def solvePancakes (path):

    with open(path, "rt") as fin:
        stuff = fin.read().splitlines()
    #stuff = path.splitlines()
    happy = '+'
    sad = '-'
    string = ""
    for i in xrange(1, len(stuff)):

        flips = 0
        for c in (stuff[i][::-1]):
            if c == sad:
                flips += 1
                temp = happy
                happy = sad
                sad = temp
        string = string + "Case #%d: %d\n" %(i, flips)
        happy = '+'
        sad = '-'

    with open("solution2 large.txt", "wt") as fout:
        fout.write(string)
