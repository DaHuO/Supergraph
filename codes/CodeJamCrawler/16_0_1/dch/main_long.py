f = open('in_long.txt', 'r')
w = open('out_long.txt', 'w')

t_count = int(f.readline())

a = [None] * t_count

for x in range(0, t_count):
    n = int(f.readline())
    if (n == 0):
        r = "INSOMNIA"
    else:
        digits = set()
        req = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        i = 0
        while digits != req:
            i += 1
            digits = digits.union(list(str(n * i)))
        if i == 0:
            r = str(n)
        else:
            r = str(n * i)
    w.write("Case #" + str(x + 1) + ": " + r + "\n")