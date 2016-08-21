import sys, math

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for case in xrange(1,1+cases):
    pancakes = list(stdin.pop(0).strip())
    flips = 0
    while len(pancakes):
        while pancakes[-1] == "+":
            pancakes.pop()
            if not len(pancakes):
                break
        if not len(pancakes):
            break
        flips += 1
        if pancakes[0] == "+":
            i = 0
            while pancakes[i] == "+":
                i += 1
            pancakes = list("-" * i) + pancakes[i:]
        else:
            newpancakes = []
            for pancake in pancakes:
                if pancake == "-":
                    newpancakes.append("+")
                elif pancake == "+":
                    newpancakes.append("-")
            newpancakes.reverse()
            pancakes = newpancakes
    print "Case #" + str(case) + ": " + str(flips)
