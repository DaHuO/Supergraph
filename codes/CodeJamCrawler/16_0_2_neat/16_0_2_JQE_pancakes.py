input = open("B-large.in", "r")
cases = int(input.readline())

def flip(sol, orig, flipped, leftmostindex, length):
    for i in range(leftmostindex, length):
        sol[i] = flipped[i]
    return sol, flipped, orig

for case in range(cases):
    pancakes = input.readline()
    plist = list(pancakes)
    pfliplist = []
    for pancake in plist:
        if pancake == '+':
            pfliplist.append('-')
        else:
            pfliplist.append('+')
    plist.reverse()
    pfliplist.reverse()
    solution = plist[:]
    steps = 0
    l = len(solution)
    
    while(True):
        try:
            bottomflip = solution.index('-')
        except ValueError:
            print("Case #{0}: {1}".format(case+1, steps))
            break
        solution, plist, pfliplist = flip(solution, plist, pfliplist, bottomflip, l)
        steps += 1