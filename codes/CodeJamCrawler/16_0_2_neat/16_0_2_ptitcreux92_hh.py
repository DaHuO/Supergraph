def main(filename):
    f = iter(open(filename, "r").readlines())

    t = int(next(f))
    for e, _ in enumerate(range(t)):
        g = (next(f).strip())
        print("Case #{}: {}".format(e+1, find(g)))


def find(n):
    sol = 0
    # if n[0] == "-":
        # sol += 1
    if n[-1] == "-":
        sol += 1

    for i, j in zip(n, n[1:]):
        if i != j:
            sol +=1
    # print(n)
    # print(sol)
    return sol
    


if __name__ == "__main__":

    filename = "testhh"
    filename = "B-small-attempt0.in"
    filename = "B-large.in"

    main(filename)