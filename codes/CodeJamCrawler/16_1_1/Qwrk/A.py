
def solve(s):
    r = s[0]
    for l in s[1:]:
        if l >= r[0]: r = l + r
        else: r = r + l
    return r


def main():
    t = int(input())
    for case in range(1, t + 1):
        print("Case #%d: %s" % (case, solve(input())))


if __name__ == "__main__":
    main()
