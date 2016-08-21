def pancake(order):
    flip = 0
    good, bad = '+', '-'
    index = len(order)
    for i in range(len(order) - 1, -1, -1):
        if order[i] == bad:
            flip += 1
            good, bad = bad, good
    return flip


N = int(input())
for i in range(N):
    print("Case #{}: {}".format(i + 1, pancake(input())))
