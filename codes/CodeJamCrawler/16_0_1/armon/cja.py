from sys import argv

def can_sleep(N):

    digits = set(str(N))
    i = 1

    while (len(digits) < 10):
        i += 1
        digits |= set(str(N*i))
        if i > 100:
            return 'INSOMNIA'

    return N*i

if __name__=='__main__':

    fin = open(argv[1], 'r')
    tnum = int(fin.readline())
    fout = open(argv[1]+'_out', 'w')

    for i, l in enumerate(fin, 1):
        fout.write('Case #{0}: {1}\n'.format(i, can_sleep(int(l))))
