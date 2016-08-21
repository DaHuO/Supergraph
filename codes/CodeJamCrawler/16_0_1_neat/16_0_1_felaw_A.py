def sheep(N):
    if N == 0:
        return 'INSOMNIA'
    num = 0
    digits = set()
    while len(digits) < 10:
        num += N
        chars = set(str(num))
        digits |= chars
    return num

for i in range(int(input())):
    N = int(input())
    print("Case #%s: %s" % (i+1, sheep(N)))