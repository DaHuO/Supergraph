t = int(input())

for x in range(t):
    pnts = []
    K, C, S = map(int, input().split())
    print("Case #" + str(x + 1) + ": ", end="")

    d = 0
    while d < K:
        p = 1
        for i in range(1, C + 1):
            p += d * pow(K, C - i)
            d += 1
            if d == K:
                break

        pnts.append(p)

    if len(pnts) > S:
        print("IMPOSSIBLE", end="")
    else:
        for p in pnts:
            print(p, end=" ")
    print()

# cks = []
# cnt = 0
#
# def flipCks(i):
#     for c in range(i, - 1, -1):
#         if cks[c] == 0:
#             cks[c] = 1
#         else:
#             cks[c] = 0
#
# for x in range(t):
#     c_cks = input()
#     lg = len(c_cks)
#     cks = [0 for y in range(lg)]
#
#     for c in range(lg):
#         if c_cks[c] == '+':
#             cks[c] = 1
#         else:
#             cks[c] = 0
#
#     cnt = 0
#     print("Case #" + str(x + 1) + ": ", end="")
#
#     for c in range(lg - 1, -1, -1):
#         if not(c == lg - 1 or cks[c] == cks[c + 1]):
#             flipCks(c)
#             cnt += 1
#
#     if not (1 in cks):
#         flipCks(lg - 1)
#         cnt += 1
#
#     print(cnt)
