T = input()
for i in range(T):
    N = input()
    if N == 0:
        print 'Case #' + str(i + 1) + ': INSOMNIA'
        continue
    count = 0
    digits = set()
    while len(digits) < 10:
        count += 1
        digits |= set(str(count * N))

    print 'Case #' + str(i + 1) + ': ' + str(count * N)
