t = int(raw_input())

def splice(n, lst):
    y = n
    lst_n = lst
    while (y != 0):
        if (lst_n[y % 10] == 0):
            lst_n[y % 10] = 1
        y //= 10
    return lst_n

for p in xrange(1, t + 1):
    n = int(raw_input())
    if (n == 0):
        print "Case #{}: INSOMNIA".format(p)
    else:
        arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        flag = False
        x = n
        while not flag:
            arr = splice (x, arr)
            s = 0
            for item in arr:
                s += item
            if (s == 10):
                print "Case #{}: {}".format(p, x)
                flag = True
            x += n