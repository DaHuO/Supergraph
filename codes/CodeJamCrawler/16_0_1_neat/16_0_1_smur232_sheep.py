with open("A-large.in", 'r') as f_in:
    cases = int(f_in.readline())
    output = ""

    for case in range(cases):
        n = int(f_in.readline())
        if n == 0:
            res = 'INSOMNIA'
        else:
            seen = set()
            m = 0
            while len(seen) != 10:
                m += 1
                seen.update(list(str(m * n)))
            res = str(m * n)

        output += "Case #{}: {}\n".format(str(case + 1), res)
        with open("output.txt", 'w') as f:
            f.write(output)
