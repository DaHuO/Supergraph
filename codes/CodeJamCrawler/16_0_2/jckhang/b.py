def pan(n):
    t = 0
    now = [i for i in n]
    while len(now) > 0:
        l = len(now)
        while now[l - 1] == '+':
            l -= 1
            if l <= 0:
                return t
        temp = ['+' if i == '-' else '-' for i in now[0:l - 1]]
        now = temp

        t += 1

    return t
t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    result = pan(n)
    print("Case #{}: {}".format(i, result))
