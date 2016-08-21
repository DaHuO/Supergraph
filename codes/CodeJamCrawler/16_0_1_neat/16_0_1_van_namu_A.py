__author__ = 'namu'
T = int(raw_input())
for case in range(1, T + 1):
    seen_digits = set()
    seen_num = []
    N = int(raw_input())
    i = 1
    res = 'INSOMNIA'
    while len(seen_digits) < 10:
        num = i * N
        seen_digits |= set(str(num))

        if num not in seen_num:
            seen_num.append(num)
            i += 1
        else:
            res = 'INSOMNIA'
            break
    else:
        res = num

    print 'Case #%d: %s' % (case, res)