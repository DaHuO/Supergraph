import fileinput

cases = [int(c) for c in list(fileinput.input())[1:]]
for i, n in enumerate(cases):
    result = "INSOMNIA"
    if n != 0:
        cur_n = n
        seen_digits = set()
        while len(seen_digits) < 10:
            result = cur_n
            seen_digits |= set([int(x) for x in str(cur_n)])
            cur_n += n
    print("Case #{}: {}".format(i + 1, result))
