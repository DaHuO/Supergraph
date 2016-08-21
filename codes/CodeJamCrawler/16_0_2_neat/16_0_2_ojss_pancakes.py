test_cases = int(raw_input())
reversal_counter = 0


def sequencer(lis):
    count = 0
    for ind, val in enumerate(lis):
        if ind == 0:
            continue
        else:
            if val is not lis[ind - 1]:
                count += 1
    if lis[-1] == '-':
        count += 1
    print count


for t in xrange(0, test_cases):
    string = str(raw_input())
    split_str = [ch for ch in string]
    print "Case #%s:" % str(t + 1),
    sequencer(split_str)
