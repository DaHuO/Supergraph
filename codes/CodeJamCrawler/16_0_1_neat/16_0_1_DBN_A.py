
fout = open('a.out', 'w')
fin = open('A-large.in', 'r')

t = int(fin.readline())
for x in range(1,t+1):
        n = int(fin.readline())
        seenNumbers = set()
        seenDigits = set()
        seeing = n
        while seeing not in seenNumbers:
            seenNumbers.add(seeing)
            tmp = seeing
            while tmp > 0:
                seenDigits.add(tmp%10)
                tmp //= 10
            if len(seenDigits) >= 10:
                break;
            seeing += n
        if len(seenDigits) < 10:
            fout.write('Case #{}: {}\n'.format(x, 'INSOMNIA'))
        else:
            fout.write('Case #{}: {}\n'.format(x, seeing))
