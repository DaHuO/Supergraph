

def sol(n):
    if not n: return 0

    if n[-1] == '-':
        if n[0] == '+':
            index = n.index('-')
            return 1 + sol(['-'] * index + n[index:])
        else:
            return 1 + sol(['+' if k == '-' else '-' for k in reversed(n)])

    else:
        return sol(n[:-1])

# assert sol(0) == "INSOMNIA"
# assert sol(1) == 10
# assert sol(2) == 90
# assert sol(11) == 110
# assert sol(1692) == 5076

def read(filepath):
    with open(filepath) as ifile:
        n = int(ifile.readline())
        for i in range(n):
            print "Case #%s:"%(i+1), sol(list((ifile.readline())))


if __name__ == "__main__":
    import clime;
    clime.start(debug=True)
