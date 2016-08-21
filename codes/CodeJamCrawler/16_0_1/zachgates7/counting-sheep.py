def case(func):
    def wrapper(i, n):
        retval = func(int(n))
        return "Case #{0}: {1}\n".format(i+1, retval)
    return wrapper


@case
def digify(n):
    if n:
        d, c = set("1234567890"), set()
        i, j = 1, n
        while c != d:
            c.update(str(n * i))
            j = n * i
            i += 1
        return str(j)
    else:
        return "INSOMNIA"


ifname = input("File: ")

with open(ifname + ".in", "r") as f:
    lines = f.readlines()
    lines.pop(0)

with open(ifname + ".out", "w") as f:
    for i, l in enumerate(lines):
        f.write(digify(i, l))
