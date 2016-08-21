TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    print("Case #", end="")
    print(tc, end=": ")
    # Special case
    if n == 0:
        print("INSOMNIA")
        continue
    i = 1; c = 0; last = 0
    a = set()
    while (len(a) < 10):
        last = n*i
        s = str(last)
        for x in s:
            a.add(x)
        i += 1
    print(last)
