def fractiles(x, y, z):
    if x == 1:
        return 1

    if y == 1:
        if x > z:
            return 'IMPOSSIBLE'
        else:
            return ' '.join(str(v) for v in range(1, x + 1))

    if z <= x - 2:
        return 'IMPOSSIBLE'
    else:
        return ' '.join(str(v) for v in range(2, x + 1))


if __name__ == "__main__":

    tc = int(input())
    for t in range(tc):
        i, j, k = [int(v) for v in input().split()]
        print("Case #{}: {}".format(t + 1, fractiles(i, j, k)))
