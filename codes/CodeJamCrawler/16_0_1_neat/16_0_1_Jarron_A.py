def count_sheep(n):
    count = 0
    n_sum = 0
    n_set = set()

    if n == 0:
        return "INSOMNIA"
    while count < 10000000:
        count += 1
        n_sum += n
        n_set |= set(list(str(n_sum)))
        if len(n_set) == 10:
            return n_sum
    return "INSOMNIA"

if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    count = 0
    with open(filename) as f:
        line = f.readline()
        while line:
            line = f.readline()
            if not line:
                continue
            count += 1
            n = int(line)
            s = str(count_sheep(n))
            print "Case #%d: %s" % (count, s)
