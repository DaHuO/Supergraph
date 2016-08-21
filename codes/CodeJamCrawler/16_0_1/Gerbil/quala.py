def result(input):
    n = input
    if n == 0:
        return 'INSOMNIA'
    r = [False] * 10
    while True:
        for i in map(int, str(n)):
            r[i] = True
        if sum(r) == 10:
            return str(n)
        n += input


if __name__ == "__main__": 
    with open('A-large.in') as f:
        with open('A-large.out', 'w') as w:
            r = f.readlines()

            for i in range(len(r) - 1):
                w.write('Case #%d: %s\n' % (i + 1, result(int(r[i + 1][:-1]))))