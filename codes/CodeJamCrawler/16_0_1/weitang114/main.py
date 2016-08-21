import fileinput

def get_digits_set(n):
    if n == 0: return 0
    s = set()
    s.add(n % 10)
    n /= 10
    while n != 0:
        s.add(n % 10)
        n /= 10
    return s
        


def run(n):
    if n == 0: return 0
    s = set()
    in_n = n
    while len(s) < 10:
        s |= get_digits_set(n)
        # print s
        n += in_n
    return n - in_n


def main():
    # inputs = [0, 1, 2, 11, 1692]
    inputs = []
    
    for line in fileinput.input():
        inputs.append(int(line.strip()))
    inputs = inputs[1:]

    for i, n in enumerate(inputs):
        nn = run(n)
        if nn == 0:
            print 'Case #%d: INSOMNIA' % (i+1)
        else:
            print 'Case #%d: %d' % (i+1, nn)
            

if __name__ == '__main__':
    main()
