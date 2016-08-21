def flipancakes(i, pan):
    p = pan[:i]
    l = len(p)
    for x in range(l):
        if p[l-1-x] == '-':
            pan[x] = '+'
        else:
            pan[x] = '-'
    return pan

def posToFlip(pan):
    pos = len(pan)
    while pan[pos-1] != '-' and pos > 0:
        pos -= 1
    return pos

def flipTopPlus(pan):
    i = 0
    while pan[i] == '+':
        pan[i] = '-'
        i += 1
    return i, pan
    

for t in range(1, input() + 1):
    pancakes = [x for x in raw_input()]
    flips = 0
    if '-' not in pancakes:
        print "Case #{}: 0".format(t)
    else:
        while '-' in pancakes:
            cx, pancakes = flipTopPlus(pancakes)
            if cx > 0:
                flips += 1

            pos = posToFlip(pancakes)
            if pos >= 0:
                pancakes = flipancakes(pos, pancakes)
                flips += 1
        print "Case #{}: {}".format(t, flips)
            
            

        
