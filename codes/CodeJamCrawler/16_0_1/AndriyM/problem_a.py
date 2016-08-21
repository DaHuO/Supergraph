

def digits(n):
    return set(map(int, str(n)))


def last_seen(n):
    max_mult = 1000
    digs = digits(n)
    current_mult = 1
    while current_mult < max_mult and len(digs) < 10:
        current_mult += 1
        digs = digs | digits(n*current_mult)

    if len(digs) == 10:
        return str(current_mult*n)
    else:
        return 'INSOMNIA'


if __name__ == '__main__':
    # for x in range(0, 1000000):
    #     print(last_seen(x))
    with open('A-large.in', 'r') as inp:
        lines = inp.readlines()

    T = int(lines[0])
    with open('A-large.out', 'w') as out:
        for i in range(1, T+ 1):
            out.write('Case #%d: %s\n' % (i, last_seen(int(lines[i]))))
