fName = 'A-large.in'
import copy
#fName = 'input_a.txt'
inpFile = open(fName)
outpFile = file('output'+fName[:7], 'w')

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']


def not_valid(list):
    summ = sum(list)
    for x in list:
        if float(x)/float(summ) > 0.5:
            return True
    return False

for T in xrange(int(inpFile.readline())):
    answer = ''
    N = int(inpFile.readline())
    P = [int(x) for x in inpFile.readline().split(' ')]
    while not all(i == 0 for i in P):
        i = P.index(max(P))
        P[i] -= 1
        answer += alphabet[i]
        if not_valid(P):
            i = P.index(max(P))
            P[i] -= 1
            answer += alphabet[i] + ' '
        else:
            answer += ' '
    outpFile.write('Case #%d: %s\n' % (T + 1, answer))

outpFile.close()
inpFile.close()
