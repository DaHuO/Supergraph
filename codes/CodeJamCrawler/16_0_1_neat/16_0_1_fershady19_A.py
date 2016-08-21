f = open('A-large.in.txt', 'r')

cases = f.readline()

dig = list('0123456789')

def CountingSheep (N):
    if (N == 0):
        return 'INSOMNIA'
    else:
        digits = list(str(N))
        i = 1
        while dig != digits:
            i += 1
            M = N*i
            digits2 = list(str(M)) + digits
            digits = sorted(list(set(digits2)))
        return M
    
i = 1   
for case in range(int(cases)):
    line = f.readline()
    print 'Case #'+str(i)+': ' + str(CountingSheep(int(line)))
    i += 1

