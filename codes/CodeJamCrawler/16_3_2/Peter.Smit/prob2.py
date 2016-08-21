import math
import sys

fin = sys.stdin
num_cases = int(fin.readline().strip())


def solve(B,M):
    if M > 2 ** (B-2):
        return None

    slides = []
    for _ in range(B):
        slides.append([0] * B)

    for i in range(B-1):
        for j in range(i+1, B-1):
            slides[i][j] = 1

    for j in range(B-2, -1, -1):
        if 2 ** (max(j-1, 0)) <= M:
            slides[j][B-1] = 1
            M -= 2 ** (j-1)
    #
    #
    # for
    # C = int(math.floor(math.log(M,2))) + 1
    #
    # for i in range(C):
    #     for j in range(i+1, C):
    #         slides[i][j] = 1
    #
    # remainder = M - (2 ** (C-1))
    #
    #
    # for i in range(C-1, -1, -1):
    #     if 2 ** i <= remainder:
    #         slides[i][C] = 1

    # left = M - 2 ** (full_slides_until-2)
    # print(left)
    #
    # for j in range(full_slides_until-1, -1, -1):
    #     if j ** 2 < left:
    #         slides[j][full_slides_until] = 1
    #         left -= j ** 2
    #
    # for j in range(min(B-1,full_slides_until+1)):
    #  slides[j][B-1] = 1

    return slides


for t in range(num_cases):
    B,M = (int(a) for a in fin.readline().strip().split())

    res = solve(B,M)
    if res is None:
        print("Case #{}: {}".format(t + 1, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(t + 1, "POSSIBLE"))
        for s in res:
            print("".join(str(a) for a in s))
