with open('A-large.in','rU') as infile:
    lines = int(infile.next())
    for i, line in enumerate(infile):
        test_case_num = i + 1
        if i == lines:
            break
        base = int(line.strip())
        digits_seen = set()
        last_seen = -1
        coefficient = 1
        while True:
            result = coefficient * base
            if last_seen == result:
                print "Case #%d: INSOMNIA" % (test_case_num)
                break
            digits_seen.update(str(result))
            if len(digits_seen) == 10:
                print "Case #%d: %d" % (test_case_num, result)
                break
            coefficient += 1
            last_seen = result