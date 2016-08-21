from itertools import product


def step(cur, init):
    ret = list()
    for char in cur:
        if char == "G":
            ret.append("G" * len(init))
        else:
            ret.append(init)
    return "".join(ret)

for t in range(1, int(input()) + 1):
    k, c, s = map(int, input().split())
    #
    # if 2 ** c > 1000:
    #     continue
    #
    # final = list()
    # for seed in ["".join(x) for x in product("GL", repeat=k)]:
    #     for level in range(1, c+1):
    #         if level == 1:
    #             tmp = seed
    #         else:
    #             tmp = step(tmp, seed)
    #         if level == c:
    #             final.append(tmp)
    # found = [False for _ in final]

    ret = []
    if c == 1:
        for i in range(k):
            ret.append(i+1)
    else:
        a = 0
        while len(ret) < s:
            ret.append(a + 1)
            a += k ** (c - 1)
    #
    # for v in ret:
    #     for i, f in enumerate(final):
    #         if f[v-1] == "G":
    #             found[i] = True
    #
    # if found.count(False) > 1 or len(ret) > s:
    #     print("test:", k, c, s)
    #     print(len(ret), s, found)

    print("Case #%d:" % t, " ".join(map(str, ret)))
