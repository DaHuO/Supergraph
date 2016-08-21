
def solve(n):
    d = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

    if n == 0:
        return 0

    m = n
    i = 1
    while True:
        s = str(m)
        for c in s:
            d[c] += 1

        flag = True
        for k in d:
            if d[k] == 0:
                flag = False
                break

        if flag:
            return m
        else:
            m += n
            i += 1

if __name__ == '__main__':
    t = int(input())

    for t_i in range(1, t + 1):
        n = int(input())
        res = solve(n)

        if res == 0:
            print("Case #{}: INSOMNIA".format(t_i))
        else:
            print("Case #{}: {}".format(t_i, res))
