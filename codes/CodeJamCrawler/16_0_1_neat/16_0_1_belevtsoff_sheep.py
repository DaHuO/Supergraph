import sys


REF = set([str(i) for i in range(10)])


def last_num(N):
    if N == 0:
        return "INSOMNIA"
    digs = set(str(N))
    last = N
    while True:
        if digs == REF:
            return last
        last += N
        digs.update(set(str(last)))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = f.readlines()

    T = int(data[0].strip())

    answers = []
    for i in range(T):
        num = last_num(int(data[i + 1]))
        answers.append(str(num))

    with open(sys.argv[2], 'w') as f:
        for i, a in enumerate(answers):
            f.write("Case #{0}: {1}\n".format(i + 1, a))
