
def make(s, c, src):
    if c == 1:
        return s

    t = ""
    for x in s:
        if x == "G":
            t += len(src) * "G"
        else:
            t += src
    return make(t, c - 1, src)


def func(s, c):
    return make(s, c, s)


def test():
    s = "LGLLL"
    c = 3
    t = func(s, c)
    print(t)
    print(len(t))
    for i in range(0, len(t), len(t) // len(s)):
        print(t[i], end="")


def solve(k, c, s):
    ans = " ".join([str(i + 1) for i in range(0, k ** c, k ** c // k)])
    assert len(ans.split()) == s
    return ans


def main():
    t = int(input())
    ans_list = []
    for i in range(t):
        k, c, s = map(int, input().split())
        ans_list.append(solve(k, c, s))

    for i, ans in enumerate(ans_list, start=1):
        print("Case #{0}: {1}".format(i, ans))

if __name__ == '__main__':
    main()
