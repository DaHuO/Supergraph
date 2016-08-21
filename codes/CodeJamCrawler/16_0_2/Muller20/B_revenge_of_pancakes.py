def solve(s):
    step = 0
    sign = '+'
    for c in s[::-1]:
        if c != sign:
            sign = c
            step += 1

    return step


if __name__ == '__main__':
    t = int(input())

    for t_i in range(1, t + 1):
        s = input()
        res = solve(s)

        print("Case #{}: {}".format(t_i, res))
