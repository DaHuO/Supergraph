def ans(n):
    if n==0:
        return 'INSOMNIA'
    chars = set(str(i) for i in range(10))
    current = n
    while True:
        chars -= set(c for c in str(current))
        if len(chars) is 0:
            return current
        current += n

t = int(input())
for testcase in range(t):
    n = int(input())
    print("Case #{}: {}".format(testcase+1, ans(n)))
