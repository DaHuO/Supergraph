import sys


class Solved(Exception):
    pass


def get_last_index(data, value):
    l = len(data)
    for index, i in enumerate(reversed(data)):
        if i == value:
            return l - index - 1


def rev(data, index):
    q = list()
    i = index
    while i >= 0:
        q.append(not data[i])
        i -= 1

    q += data[index+1:]
    return q


def solve(data):
    counter = 0
    data = [bool(x == '+') for x in data]

    while not all(data):
        index = get_last_index(data, False)
        if data[0]:
            data = rev(data, data.index(False)-1)
        else:
            data = rev(data, index)

        counter += 1

    raise Solved(counter)


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        try:
            solve(list(sys.stdin.readline().strip()))
        except Solved as e:
            print('Case #{}: {}'.format(i+1, e))
