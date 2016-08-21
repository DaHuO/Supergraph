def total_flip(cakes):
    if cakes == "": return 0

    new_cake = cakes[0]
    for cc in cakes[1:]:
        if cc != new_cake[-1]:
            new_cake = new_cake + cc

    new_cake = new_cake.rstrip('+')
    # print cakes, new_cake
    return len(new_cake)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    count = 0
    with open(filename) as f:
        line = f.readline()
        while line:
            line = f.readline().strip('\n')
            if not line: 
                continue
            count += 1
            print "Case #%d: %s" % (count, total_flip(line))

