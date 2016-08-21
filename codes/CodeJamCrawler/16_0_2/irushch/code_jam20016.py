def find_flips(st):
    if not st:
        return 0

    if '+' not in st:
        return 1
    if '-' not in st:
        return 0
    if len(st) == 2:
        return {'-+': 1, '+-': 2}.get(st, 0)

    result = 0
    n = 0
    to_flip = ''
    for n, i in enumerate(st, 1):
        if i == '+':
            to_flip += i

        if i == '-':
            if to_flip:
                to_flip += i
            if (n >= len(st) or st[n] == '+'):
                if to_flip:
                    if len(to_flip) not in [1, 2]:
                        to_flip = ''.join([{'-': '+', '+': '-'}.get(x)
                                           for x in to_flip])
                        result += 1
                    result += find_flips(to_flip)
                else:
                    result += find_flips(st[:n])
                break
    if n:
        result += find_flips(st[n:])
    return result


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        # read a list of integers
        s = raw_input()
        print 'Case #{}: {}'.format(i, find_flips(s))

