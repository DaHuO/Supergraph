t = int(input())
for case in range(t):
    n = int(input())
    s = set()
    ans = 'INSOMNIA'
    for i in range(75):
        x = n * i
        while x > 0:
            s.add(x % 10)
            x //= 10
            if len(s) == 10:
                ans = n * i
                break
        if len(s) == 10:
            break
    print('Case #', case + 1, ': ', ans, sep = '')
