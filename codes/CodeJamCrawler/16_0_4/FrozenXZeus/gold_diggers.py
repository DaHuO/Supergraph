with open("D-small-attempt0.in") as ifp, open("derp.out", "w") as ofp:
    t = int(ifp.readline())
    for i in range(t):
        lists = list(map(int, ifp.readline().strip().split()))
        k = lists[0]
        c = lists[1]
        s = lists[2]

        case_number = i + 1
        to_clean = " ".join(map(str, range(1, s+1)))
        ofp.write("Case #{}: {}\n".format(case_number, to_clean))