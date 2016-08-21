T = int(input())
for t in range(1,T+1):
    print("Case #%d: " % t, end="")
    n = int(input())
    s = set()
    x = 0
    for i in range(75):
        x += n
        y = list(str(x))
        s.update(y)
        if len(s) == 10:
            break
    if len(s) == 10:
        print(x)
    else:
        print("INSOMNIA")
