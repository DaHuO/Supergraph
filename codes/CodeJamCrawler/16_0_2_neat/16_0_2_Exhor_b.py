fo = open('blarge.txt','w')
fi = open('B-large.in','r')
T = int(fi.readline())
for c in range(1, T+1):
    pancakes = fi.readline()
    pancakes = pancakes[0:-1]
    flips = 0
    done = False
    while not done:
        if sum([1 for l in pancakes if l == '+']) == len(pancakes):
            fo.write('Case #' + str(c) + ': ' + str(flips) + '\n')
            done = True
        else:
            flips = flips + 1
            p1 = pancakes[0]
            toflip = 0
            for l in pancakes:
                if l == p1:
                    toflip = toflip + 1
                else:
                    break
            if p1 == '+':
                pancakes = "-" * toflip + pancakes[toflip:]
            else:
                pancakes = "+" * toflip + pancakes[toflip:]



