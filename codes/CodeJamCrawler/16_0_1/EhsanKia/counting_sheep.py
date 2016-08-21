import string

T = int(raw_input())

for case in range(T):
    N = int(raw_input())
    digits = set()

    if N == 0:
        print "Case #{}: {}".format(case + 1, "INSOMNIA")
        continue

    i = 0
    while len(digits) < 10:
        i += 1
        digits.update(str(i * N))

    print "Case #{}: {}".format(case + 1, i * N)
