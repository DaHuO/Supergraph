def resolve(line):
    debug('Starting for ' + line)
    n_int = int(line)
    if not n_int:
        return 'INSOMNIA'

    n_str = line
    viewed = set(n_str)

    i = 2
    while len(viewed) < 10:
        n = n_int * i
        debug(n)
        viewed = viewed.union(str(n))
        i += 1

    return n


def main():
    get_line()  # dicard first

    line = get_line()
    i = 1
    while line:
        print 'Case #{}: {}'.format(i, resolve(line))
        line = get_line()
        i += 1


def debug(*args):
    pass  # print ' '.join(map(str, args))


def get_line():
    try:
        return raw_input()
    except EOFError:
        return None


if __name__ == '__main__':
    main()
    


