def getans(x):
    s = set();
    dx = x
    while True:
        x_s = str(x)
        s.update(x_s)
        if len(s) == 10: break
        x += dx
    return x

T = input()

for icase in range(1, T + 1):
    x = input()
    if x == 0:
        print("Case #" + str(icase) + ": INSOMNIA")
    else:
        print("Case #" + str(icase) + ": " + str(getans(x)))
