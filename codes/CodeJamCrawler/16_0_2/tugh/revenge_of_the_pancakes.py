T = int(input())

for t in range(1, T+1):
    P = input()

    flips = 0
    state = 1

    x = None # pancake as a number
    for p in P[::-1]:
        if p == "-":
            x = -1*state
        else:
            x = state

        if x == -1:
            flips += 1
            state *= -1


    print("Case #%d: %d" % (t, flips))