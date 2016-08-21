def solve():
    f = open("A-large.in", "r")
    T = int(f.readline())
    out = open("output.txt", "w")

    for case in range(T):
        S = f.readline().strip()
        l = []
        r = []
        l.append(S[0])
        for letter in S[1:]:
            if letter >= l[-1]:
                l.append(letter)
            else:
                r.append(letter)
        print("Case #%d: " % (case + 1), end='')
        out.write("Case #%d: " % (case + 1))

        while len(l) > 0:
            letter = l.pop()
            print("%s" % (letter), end='')
            out.write("%s" % (letter))
        for x in r:
            print("%s" % (x), end='')
            out.write("%s" % (x))
        print()
        out.write("\n")

solve()