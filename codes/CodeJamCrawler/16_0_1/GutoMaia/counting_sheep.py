
def counter(val):
    saw = set([])
    i = 0

    while len(saw) < 10:
        n = (i + 1) * val
        saw.update([int(m) for m in list(str(n))])
        yield n, saw, len(saw) == 10
        i += 1
        if i > 100:
            break

def counting_sheep(val):
    if val == 0:
        return 'INSOMNIA'
    try:
        f = counter(val)
        while True:
            n, sees, sleep = f.next()
    except StopIteration:
        return n

def counting_sheep_file(filename):
    finput = open(filename, 'r')
    fouput = open('%s_output' % filename, 'w')

    num = int(finput.readline())
    i = 1
    while i <= num:
        guess = int(finput.readline())
        n = counting_sheep(guess)
        output = 'Case #%s: %s\n' % (i, n)
        fouput.write(output)
        i += 1

    finput.close()
    fouput.close()

if __name__ == '__main__':
    import sys
    counting_sheep_file(sys.argv[1])
