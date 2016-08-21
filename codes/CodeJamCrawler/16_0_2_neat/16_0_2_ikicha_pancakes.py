def remove_last_trues(data):
    if False not in data:
        return []
    data.reverse()
    idx = data.index(False)
    if idx >= 0:
        data = data[idx:]
    data.reverse()
    return data


def solve(data):
    idx = 0
    data = remove_last_trues(data)
    while len(data) > 0:
        data = map(lambda x: not x, data)
        idx += 1
        data = remove_last_trues(data)
    return idx


def main():
    with open("B-input.in") as fin:
        with open("B-output.out", "w") as fout:
            n = int(fin.readline())
            for i in range(0, n):
                data = fin.readline().strip()
                data = map(lambda c: c == '+', data)
                fout.write("Case #%d: %d\n" % (i + 1, solve(data)))


main()
