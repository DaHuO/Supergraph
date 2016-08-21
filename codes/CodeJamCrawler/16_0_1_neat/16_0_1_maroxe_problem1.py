def f(i):
    if i == 0: return 'INSOMNIA'
    seen = [1] * 10
    r = 0
    c = i
    while True:
        for x in str(c): seen[int(x)] = 0
        if sum(seen) == 0: return str(c)
        c += i
        r += 1

t=input()
numbers = [int(input()) for _ in range(t)]

template = "Case #%d: %s"
for (i, r) in enumerate(map(f, numbers)):
    print(template % (i+1,r))

