#import time
#fName = 'input'
#fName = 'A-large-practice.in'
fName = 'A-large.in'
inpFile = open(fName)
outpFile = file('output'+fName[:7], 'w')


def addToMemory(N):
    global inMemory
    for digit in N:
        if inMemory.count(digit) == 0:
            inMemory.append(digit)

for T in xrange(int(inpFile.readline())):
#    t0 = time.time()
    Nstr = inpFile.readline()
    if Nstr[-1] == '\n':
        Nstr = Nstr[:-1]
    if Nstr == '0':
        outpFile.write('Case #' + str(T+1) + ': INSOMNIA\n')
        continue
    inMemory = []
    addToMemory(Nstr)
    i = 1
    while len(inMemory) != 10:
        i += 1
        addToMemory(str(i * int(Nstr)))
#        if time.time()-t0 > 11.0:
#            outpFile.write('Case #' + str(T+1) + ': INSOMNIA\n')
#            continue
    outpFile.write('Case #' + str(T+1) + ': ' + str(i * int(Nstr)) + '\n')

outpFile.close()
inpFile.close()