t = int(input())
cks = []
cnt = 0

def flipCks(i):
    for c in range(i, - 1, -1):
        if cks[c] == 0:
            cks[c] = 1
        else:
            cks[c] = 0

for x in range(t):
    c_cks = input()
    lg = len(c_cks)
    cks = [0 for y in range(lg)]

    for c in range(lg):
        if c_cks[c] == '+':
            cks[c] = 1
        else:
            cks[c] = 0

    cnt = 0
    print("Case #" + str(x + 1) + ": ", end="")

    for c in range(lg - 1, -1, -1):
        if not(c == lg - 1 or cks[c] == cks[c + 1]):
            flipCks(c)
            cnt += 1

    if not (1 in cks):
        flipCks(lg - 1)
        cnt += 1

    print(cnt)
