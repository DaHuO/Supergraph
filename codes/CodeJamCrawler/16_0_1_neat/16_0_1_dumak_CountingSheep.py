def solve():
    n = int(input())

    for i in range(n):
        start_num = int(input())
        if start_num == 0:
            print("Case #%s: INSOMNIA" % (i + 1))
        else:
            digits = set()
            j = 1
            while len(digits) < 10:
                digits.update(list(str(start_num * j)))
                j += 1
            print("Case #%s: %s" % (i + 1, start_num * (j - 1)))

solve()