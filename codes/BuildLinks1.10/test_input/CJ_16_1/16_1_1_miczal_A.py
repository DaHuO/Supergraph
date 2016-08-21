T = int(input())
for t in range(T):
    S = input()
    last_w = ''
    for c in S:
        if last_w == '':
            last_w += c
        elif last_w[0] > c:
            last_w += c
        else:
            last_w = c + last_w
    print("Case #%d: %s" % ((t+1), last_w))
