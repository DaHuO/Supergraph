def f(s):
    i = 0
    pc = ''
    t = 0
    while i < len(s):
        if not pc == s[i]:
            pc = s[i]
            t = t + 1
        i = i + 1
    if s[-1:] == '+':
        t = t - 1
    return t

def main():
    T = int(raw_input())
    t = 1
    while t <= T:
        s = raw_input().strip()
        ans = f(s)
        print "Case #{0}: {1}".format(t, ans)
        t = t + 1

if __name__ == "__main__":
    main()