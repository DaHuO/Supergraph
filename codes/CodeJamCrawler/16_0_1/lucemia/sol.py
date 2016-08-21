

def sol(n):
    if n == 0: return "INSOMNIA"
    x = set()

    t = 0
    for i in range(100):
        t += n
        x.update(str(t))

        if len(x) == 10:
            return t
            break


# assert sol(0) == "INSOMNIA"
# assert sol(1) == 10
# assert sol(2) == 90
# assert sol(11) == 110
# assert sol(1692) == 5076

def read(filepath):
    with open(filepath) as ifile:
        n = int(ifile.readline())
        for i in range(n):
            print "Case #%s:"%(i+1), sol(int(ifile.readline()))


if __name__ == "__main__":
    import clime;
    clime.start(debug=True)
