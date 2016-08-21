T = int(input().strip())

for t in range(T):
    s = input().strip()

    flips = 0
    make_ones = True
    for ch in reversed(s):
        if make_ones and ch == '-':
                flips += 1
                make_ones = False
        if not make_ones and ch == '+':
                flips += 1
                make_ones = True

    print("Case #{}: {}".format(t+1, flips))
