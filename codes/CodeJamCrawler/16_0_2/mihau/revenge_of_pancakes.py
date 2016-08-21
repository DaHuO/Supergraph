def xor(a, b):
    if a == b:
        return False
    else:
        return a or b


def solve(b):
    flipped = False
    flipz = 0
    id = -1
    i = b[id]
    while id > -len(b):
        should_flip = False
        while id > -len(b) and not xor(i, flipped):
            should_flip = True
            id -= 1
            i = b[id]
        if should_flip:
            flipped = not flipped
            flipz += 1
        while id > -len(b) and xor(i, flipped):
            id -= 1
            i = b[id]
    if not xor(i, flipped):
        flipz += 1
    return flipz


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        b = map(lambda x: True if x == "+" else False, input())
        print("Case #{0}: {1}".format(i + 1, solve(list(b))))
