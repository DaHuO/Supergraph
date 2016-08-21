LEFT = 1
RIGHT = -1

def find_ocr(pancakes, ch, sd):
    i=0
    if sd == RIGHT:
        i=len(pancakes)-1
    while i >= 0 and i < len(pancakes) and pancakes[i] != ch:
        i += sd
    # print "find_ocr: ", pancakes, sd
    # print i
    if i == -1 or sd == len(pancakes):
        return -1
    return i

def flip(pancakes, t):
    pc = pancakes[t+1:]
    i=0
    while i <= t:
        p = '-' if pancakes[i] == '+' else '+'
        pc = p + pc
        i += 1
    # print "flip: ", pancakes, t, pc
    return pc


T = input()
for case in range(0,T):
    pancakes = raw_input()
    ret = 0
    at = 1
    while True:
        i = find_ocr(pancakes, '-', LEFT)
        j = find_ocr(pancakes, '-', RIGHT)
        # print i,j
        at += 1
        if j == -1:
            break
        if i > 0:
            pancakes = flip(pancakes, i-1)
            # print pancakes
            ret += 1
        if i != j or j == 0:
            pancakes = flip(pancakes, j)
            ret += 1
        # print pancakes
    output = "Case #%s: %s" % (case+1, ret)
    print output