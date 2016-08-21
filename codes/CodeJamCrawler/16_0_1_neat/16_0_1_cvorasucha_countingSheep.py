def countSheep(filename):
    f = open(filename, 'r')
    g = open('countingSheep_out_large.txt', 'w')
    n_line = int(f.readline())

    for i in range(1, n_line + 1):
        seen_num, seen_dig = set(), set()
        init_n = int(f.readline())
        n, n_iter = init_n, 1
        is_done = False
        while n not in seen_num:
            seen_dig = seen_dig.union(list(str(n)))
            if len(seen_dig) == 10:
                is_done = True
                g.write("Case #" + str(i) + ": " + str(n) + '\n')
                break
            seen_num.add(n)
            n_iter += 1
            n = n_iter * init_n
        if not is_done:
            g.write("Case #" + str(i) + ": INSOMNIA\n")

countSheep("A-large.in")
#countSheep("countingSheep_in.txt")