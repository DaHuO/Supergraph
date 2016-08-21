def read():
    with open('A-large.in') as f:
        return f.readlines()


def write(lines):
    with open('result.txt', 'w') as f:
        i = 1
        for line in lines:
            f.write('Case #' + str(i) + ': ' + str(line) + '\n')
            i += 1


def solve(data):
    res = []
    for num in data:
        s = set()
        i = 1
        while True:
            if num == 0:
                res.append('INSOMNIA')
                break
            for el in list(str(num * i)):
                s.add(el)
            if len(s) == 10:
                res.append(num * i)
                break
            i += 1
    return res


if __name__ == '__main__':
    data = list(map(int, read()))[1:]
    write(solve(data))
