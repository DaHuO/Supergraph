import sys

stdin = sys.stdin

T = int(stdin.readline())

for i in range(T):
    N = stdin.readline()
    ps = [int(p) for p in stdin.readline().split(" ")]

    senate_count = sum(ps)

    greatest_p = None
    greatest_indexes = []
    print("Case #{}: ".format(i + 1), end="")
    while senate_count > 2:
        for i, p in enumerate(ps):
            if not greatest_p or p >= greatest_p:
                if not greatest_p or p > greatest_p:
                    greatest_indexes = []
                greatest_p = p
                greatest_indexes.append(i)

        assert(greatest_p <= senate_count//2)

        if(len(greatest_indexes) % 2 == 1):
            chosen = greatest_indexes[0]
            ps[chosen] -= 1
            senate_count -= 1
            print(chr(chosen + 65), end="")
        else:
            senate_count -= len(greatest_indexes[-2:])
            for index in greatest_indexes[-2:]:
                ps[index] -= 1
                print(chr(index + 65), end="")
        print(" ", end="")

        greatest_p = None
        greatest_indexes = []

        assert(senate_count == sum(ps))

    left = list(filter(lambda tup: tup[1] > 0, enumerate(ps)))
    if len(left) == 2:
        print(chr(left[0][0] + 65), end="")
        print(chr(left[1][0] + 65), end="")
    elif len(left) == 1:
        assert(False)
    print("")

