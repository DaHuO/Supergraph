cache = {}


def smallest_divisor(n):
    idx = 2
    if n in cache:
        return cache[n]
    while idx * idx <= n:
        if n % idx == 0:
            cache[n] = idx
            return idx
        idx += 1
    cache[n] = 1
    return 1


def solve(n, j):
    p = ["1"]
    for i in range(0, n - 2):
        newer = []
        for s in p:
            newer.append(s + "0")
            newer.append(s + "1")
        p = newer
    p = map(lambda c: c + "1", p)
    base_data = map(make_all_base, p)
    base_data_with_label = map(lambda l: (l[-1], l), base_data)
    coin_jam = []
    for o, l in base_data_with_label:
        if len(coin_jam) == j:
            break
        for i in l:
            if smallest_divisor(i) == 1:
                break
        else:
            coin_jam.append((o, map(smallest_divisor, l)))

    result = ""
    for (o, l) in coin_jam:
        result += str(o) + " " + " ".join(map(str, l)) + "\n"
    return result


def make_all_base(data):
    result = []
    for base in range(2, 10 + 1):
        result.append(int(data, base=base))
    return result


def main():
    with open("C-input.in") as fin:
        with open("C-output.out", "w") as fout:
            t = int(fin.readline())
            for i in range(0, t):
                n, j = map(int, fin.readline().strip().split(" "))
                fout.write("Case #%d:\n%s\n" % (i + 1, solve(n, j)))


main()
