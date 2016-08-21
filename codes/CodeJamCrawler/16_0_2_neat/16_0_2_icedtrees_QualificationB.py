t = int(raw_input())
for c in range(t):
    line = raw_input()
    flips = 0
    for ch in line[::-1]:
        b = 0 if ch == "+" else 1
        if (b + flips) % 2 == 1:
            flips += 1
    print "Case #{}: {}".format(c+1, flips)