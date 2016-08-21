def run(test):
    if test == 0:
        return "INSOMNIA"
    digits = set(str(test))
    answer = set(map(str, range(10)))
    noanswer = True
    i = 1
    while noanswer:
        i += 1
        if digits == answer:
            noanswer = False
            return "%s" % (test * (i - 1))
        digits.update(set(str(test * i)))

t = int(raw_input("").rstrip())
for i in range(t):
    print "Case #%s: %s" % (i + 1, run(int(raw_input("").rstrip())))
