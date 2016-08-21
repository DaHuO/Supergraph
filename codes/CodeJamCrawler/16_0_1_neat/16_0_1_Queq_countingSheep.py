def checkDigits(x, c):
    for j in range(0, len(x)):
        c |= 2**int(x[j])
    return c

def countingSheep(path):
    N = [int(line.rstrip('\n')) for line in open(path)]
    c = 0
    for n in range(1, N[0]+1):
        digitCount = 0
        for i in range(1, 101):
            a = i * N[n]
            digitCount = checkDigits(str(a), digitCount)
            if digitCount == 1023:
                output.write('Case #{}: {}\n'.format(n, a))
                print 'Case #{}: {}\n'.format(n, i)
                break
            if i == 100 and digitCount < 1023:
                output.write('Case #{}: INSOMNIA\n'.format(n))
                print 'Case #{}: INSOMNIA\n'.format(n)
                break

output = open('output.txt', 'w')
countingSheep('A-small-attempt4.in')
output.close()
