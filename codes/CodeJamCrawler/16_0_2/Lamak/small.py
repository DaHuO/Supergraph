import random
fw = open("output.out", "w")

def setBit(b, i, v):
    mask = 1 << i
    b &= ~mask
    if v:
        b |= mask
    return b

def isSet(b, i):
    return (b & 1 << i) > 0

def getBinary(b, l = -1):
    s = ''
    while b > 0:
        s = str(b % 2) + s
        b = b / 2
    if l > -1:
        while len(s) < l:
            s = '0' + s
    return s

def getCases():
    with open("B-large.in") as f:
        lines = f.read().splitlines() 
        T = int(lines[0])
        for t in range(1, T + 1):
            s = lines[t]
            yield {'t': t, 's': s}

def getMyCases():
    for i in range(0,100):
        x = random.getrandbits(100)
        s = ''
        for j in range(0, 100):
            s = ('+' if isSet(x, j) else '-') + s
        yield {'t': 1, 's': s}
        

for T in getCases():

    b = 0
    L = len(T['s'])
    for i in range(0, L):
        if (T['s'][i] == '+'):
            b = setBit(b, L-1-i, 1)
    #print 'bin:' + getBinary(b, L)

    steps = 0
    for i in range(0, L):
        if not isSet(b, i):
            stepped = False
            for j in range(L - 1, i, -1):
                if isSet(b, j):
                    b = setBit(b, j, 0)
                    if not stepped:
                        stepped = True
                        steps += 1
                else:
                    break
            b1 = b
            for j in range(L - 1, i - 1, -1):
                b1 = setBit(b1, j, 0 if isSet(b, L - 1 + i - j) else 1)
            b = b1
            steps += 1
        #print 'bin:' + getBinary(b, L), 'steps:', steps
                
    #print 'Case #' + str(T['t']) + ': ' + str(steps)
    fw.write('Case #' + str(T['t']) + ': ' + str(steps) + '\n')


fw.close()
