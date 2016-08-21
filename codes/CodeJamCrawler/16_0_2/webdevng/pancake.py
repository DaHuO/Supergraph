pencount = 0
def pancake_flip(tower, casenum):
    global pencount
    if "-" not in tower:
        return_count(casenum)
    elif "+" not in tower:
        pencount += 1
        return_count(casenum)
    else:
        tmp = [i for i, x in enumerate(tower) if i+1 != len(tower) and x != tower[i+1]]
        newtower = [flip(x) for x in tower[:tmp[0]+1]] + [x for x in tower[tmp[0]+1:]]
        pencount += 1
        pancake_flip(''.join(newtower), casenum)

def flip(p):
    return '-' if p == '+' else '+'

def return_count(count):
    global pencount
    print "Case #%s: %s" % (str(count), str(pencount))
    pencount = 0
    return


fo = open("B-large.in", "rw+")
line = fo.readlines()
lines = [x.split('\n')[0] for x in line]
lines.pop(0)

count = 0
for case in lines:
    count += 1
    pancake_flip(case, count)
