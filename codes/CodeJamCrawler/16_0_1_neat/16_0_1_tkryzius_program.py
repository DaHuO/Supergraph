fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

def count_digits(n):
    digits = 0
    n = str(n)
    for i in xrange(len(n)):
        digits |= 1<<int(n[i])
    return digits

for i in xrange(t):
    n = int(fin.readline())
    if n == 0:
        answer = 'INSOMNIA'
    else:
        s = 1
        digits = 0
        while digits < 1023:
            number = s*n
            digits |= count_digits(number)
            s += 1
        answer = number
    fout.write('Case #' + str(i + 1) + ': ' + str(answer) + '\n')

fout.close()
