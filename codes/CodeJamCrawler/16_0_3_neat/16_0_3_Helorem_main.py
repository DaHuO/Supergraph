primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def doit(n, j):
    res = []
    base_pattern = "1" + ("0" * (n - 2)) + "1"
    pattern = base_pattern
    base_pattern_num = int(base_pattern, 2)
    limit = int("1" * n)
    i = 0
    while int(pattern) <= limit:
        divisers = []
        ok = True
        for b in xrange(1, 10):
            val = int(pattern, b + 1)
            ok2 = False
            for p in primes:
                if val % p == 0:
                    divisers.append(str(p))
                    ok2 = True
                    break
            if not ok2:
                ok = False
                break
        if ok:
            #print "%s : %s" % (pattern, " ".join(divisers))
            res.append("%s %s" % (pattern, " ".join(divisers)))
            i += 1
            if i >= j:
                break
        num_pattern = int(pattern, 2) + 1
        num_pattern |= base_pattern_num
        pattern = "{0:b}".format(num_pattern)
    if len(res) >= j:
        return "\n".join(res)
    else:
        return "IMPOSSIBLE, found %d" % len(res)

def test(res):
    line_index = 1
    for line in res.split("\n"):
        pattern, divisers_str = line.split(" ", 1)
        divisers = divisers_str.split(" ")
        print line_index, pattern
        for b in range(1, 10):
            base = b + 1
            num_in_base = int(pattern, base)
            diviser_index = b - 1
            diviser = int(divisers[diviser_index])
            if num_in_base % diviser == 0:
                print "    base %d : %d can divide %d" % (base, diviser, num_in_base)
            else:
                print "    ERROR !!!!!!! base %d : %d cannot divide %d" % (base, diviser, num_in_base)
                exit
        line_index += 1


nb_tests = int(raw_input())
for i in xrange(nb_tests):
    line = raw_input()
    n, j = line.split(" ", 1)
    res = doit(int(n), int(j))
    print "Case #%d:\n%s" % (i + 1, res)
    #test(res)
