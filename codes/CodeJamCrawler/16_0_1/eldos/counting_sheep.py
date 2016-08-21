cases = int(input())
for i in range(cases):
    n = int(input())
    m = 0
    digits = set()
    while len(digits) != 10:
        m += n
        digits.update(map(int, list(str(m))))
        if n == 0:
            break
    if n == 0:
        print("Case #%d: INSOMNIA" % (i+1))
    else:
        print("Case #%d: %d" % (i+1, m))