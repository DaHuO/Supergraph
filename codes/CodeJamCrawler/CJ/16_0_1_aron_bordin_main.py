for t in range(int(input())):
    n = int(input())

    digits = []
    if n == 0:
        print('Case #%d: INSOMNIA' % (t + 1))
        continue

    i = 0
    while True:
        i += 1
        v = n * i
        d = str(v)
        for l in d:
            if l not in digits:
                digits.append(l)

        if len(digits) == 10:
            print('Case #%d: %d' % (t + 1, v))
            break
