def main(filename):
    f = iter(open(filename, "r").readlines())

    t = int(next(f))
    for e, _ in enumerate(range(t)):
        g = int(next(f).strip())
        print("Case #{}: {}".format(e+1, find(g)))


def find(n):
    if n == 0:
        return "INSOMNIA"
    figures = {str(i):0 for i in range(10)}
    j = 0
    for _ in range(1000000):
        j = j +n

        for k in str(j):
            figures[k] = 1

        if set(list(figures.values())) == set([1]):
            return j


if __name__ == "__main__":

    filename = "test"
    filename = "A-small-attempt0.in"
    
    filename = "A-large.in"
    main(filename)