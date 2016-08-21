import sys


class Solved(Exception):
    pass


def base10toN(number, base):
    out = []
    o = number
    while o:
        rest = o % base
        # print(rest, o)
        out.append(str(rest))
        o = o // base

    return ''.join(reversed(out))


def baseNto10(number, base):
    o = 0
    for index, i in enumerate(reversed(str(number))):
        if index == 0:
            o += int(i)
        else:
            o += (base ** (int(index))) * int(i)

    return o


def is_prime(n):
    for i in range(3, round(n**0.5)+2):
        if n % i == 0:
            return i
    return True


def solve(i):
    to2 = str(base10toN(i, 2))
    if to2[0] != '1' or to2[-1] != '1':
        return

    ret = check_Nto10(to2)
    if ret is False:
        return

    raise Solved('{} {}'.format(to2, ' '.join(map(str, ret))))

def check_Nto10(number):
    r = []
    for j in range(2, 11):
        t = baseNto10(number, j)
        d = is_prime(t)
        if d is True:
            return False

        r.append(d)

    return r

if __name__ == '__main__':
    t = 0
    print('Case #1:')
    for i in range(int(sys.stdin.readline())):
        L, limit = map(int, sys.stdin.readline().strip().split(' '))
        for j in range(32796, 65535):
            try:
                solve(j)
            except Solved as e:
                print(e)
                t += 1
                if t == limit:
                    break
