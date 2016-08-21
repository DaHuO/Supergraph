

def resolve(line):
    r = line[0]
    for c in line[1:]:
        a = r + c
        b = c + r       
        r = max(a, b)
    return r


#########################


def main():
    T = int(get_line())
    for t in xrange(T):
        print 'Case #{}: {}'.format(t+1, resolve(raw_input()))

## Trash:

def _main():
    T = int(get_line())

    line = get_line()
    i = 1
    while line:
        print 'Case #{}: {}'.format(i, resolve(line))
        line = get_line()
        i += 1


def get_line():
    try:
        return raw_input()
    except EOFError:
        return None


if __name__ == '__main__':
    main()
