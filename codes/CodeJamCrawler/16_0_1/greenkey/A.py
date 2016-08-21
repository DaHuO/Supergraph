import fileinput

def counting_sheep(n):
    n = int(n)
    if n == 0:
        return "INSOMNIA"

    seen_digits = set(str(n))
    xn = n
    while len(seen_digits) < 10:
        xn += n
        seen_digits = seen_digits | set(str(xn))
    return xn

lines = [l.strip() for l in fileinput.input()]
for (i, l) in enumerate(lines[1:]):
    print("Case #{}: {}".format(i+1,counting_sheep(l)))