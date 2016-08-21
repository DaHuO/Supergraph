import fileinput

def count(n):
    if n == 0:
        return "INSOMNIA"
    d = set()
    c = 0
    while True:
        c += n
        d.update(str(c))
        if len(d) == 10:
            return c

fin = fileinput.input()
N = int(next(fin))
for i in range(1, N + 1):
    print("Case #{}: {}".format(i, count(int(next(fin)))))
