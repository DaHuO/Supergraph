import sys


class Solved(Exception):
    pass


def solve(data):
    if data == 0:
        raise Solved('INSOMNIA')

    out = set()
    for i in range(1, 101):
        t = data * i
        out.update(list(str(t)))
        if len(out) == 10:
            raise Solved(t)

    raise Solved('INSOMNIA2')


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            solve(int(sys.stdin.readline()))
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
