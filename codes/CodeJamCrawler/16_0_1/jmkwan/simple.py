import fileinput

def answer(n):
    if n == 0:
        return "INSOMNIA"
    x = n
    seen = set()
    while len(seen) != 10:
        seen.update(str(x))
        x += n
    return x - n

if __name__ == '__main__':
    for n, i in enumerate(fileinput.input()):
        if n == 0:
            continue
        print("Case #%d: %s" % (n, answer(int(i))))
