def last_count(n):
    if n == 0:
        return "INSOMNIA"
    count = n
    a = 1
    digits_seen = [False] * 10
    all_seen = False
    while not all_seen:
        stripped_count = count  # compute digits seen for this count
        while stripped_count > 0:
            digits_seen[stripped_count % 10] = True
            stripped_count /= 10
        all_seen = True  # check whether all digits were seen
        for flag in digits_seen:
            if not flag:
                all_seen = False
                break
        if all_seen:  # if all seen, return the last count, otherwise proceed to the next
            return "{}".format(count)
        else:
            a += 1
            count = a * n

t = int(raw_input())  # The number of test cases.
for i in xrange(1, t + 1):
    print "Case #{}: {}".format(i, last_count(int(raw_input())))