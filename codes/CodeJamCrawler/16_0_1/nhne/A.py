inputfile = "A-large.in"
#inputfile = "sample.txt"
fin = open(inputfile, 'r')
fou = open('out.txt', 'w')

T = fin.readline()

for tc in xrange(int(T)):
    N = int(fin.readline())
    sumN = 0
    sets = set()
    ans = 'INSOMNIA'

    
    for i in xrange(1, 10 ** 6):
        sumN += N
        for s in str(sumN):
            sets.add(s)
        if len(sets) == 10:
            ans = i * N
            break

    fou.write('Case #' + str(tc + 1) + ': ' + str(ans) + '\n')



fou.close()
fin.close()
