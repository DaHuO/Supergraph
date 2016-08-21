import random
fw = open("output.out", "w")

def getCases():
    with open("A-large.in") as f:
        lines = f.read().splitlines() 
        T = int(lines[0])
        for t in range(1, T + 1):
            s = lines[t]
            yield {'t': t, 's': s}

def getMyCases():
    yield {'t': 1, 's': ''}
        

for T in getCases():

    m = T['s'][0] + ''
    for c in T['s'][1:]:
        if c >= m[0]:
            m = c + m
        else:
            m = m + c

    print 'Case #' + str(T['t']) + ': ' + m
    fw.write('Case #' + str(T['t']) + ': ' + m + '\n')


fw.close()
