fw = open("output.out", "w")

def getDigits(x):
    yield x % 10
    while int(x / 10) != 0:
        x = int (x / 10)
        yield x % 10

def getCases():
    fr = open("A-large.in", "r")
    T = int(fr.readline())
    for t in range(1, T + 1):
        n = int(fr.readline())
        yield {'t': t, 'n': n}
    fr.close()

def getWorstCases():
    T = 1000001
    for t in range(1, T + 1):
        yield {'t': t, 'n': t}
        

for T in getCases():
    bins = 0

    if T['n'] == 0:
        fw.write('Case #' + str(T['t']) + ': INSOMNIA\n')
    else:
        x = T['n']
        while bins != 1023:
            for digit in getDigits(x):
                bins = bins | (2 ** digit)

            x = x + T['n']

        fw.write('Case #' + str(T['t']) + ': ' + str(x - T['n']) + '\n')


fw.close()
