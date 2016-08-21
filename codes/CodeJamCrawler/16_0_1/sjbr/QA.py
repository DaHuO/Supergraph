def solve():
    f = open("A-large.in", "r")
    T = int(f.readline())
    out = open("output.txt", "w")

    for case in range(T):
        N = int(f.readline())
        if N == 0:
            print("Case #%d: %s" % (case+1, "INSOMNIA"))
            out.write("Case #%d: %s\n" % (case+1, "INSOMNIA"))
            continue
        digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        mult = 1
        while 0 in digits:
            number = mult * N
            while number > 0:
                digits[number % 10] += 1
                number = number // 10
            mult += 1

        print("Case #%d: %d Multiple %d" % (case + 1, N * (mult - 1), mult))
        out.write("Case #%d: %d\n" % (case + 1, N * (mult - 1)))


solve()
