__author__ = 'vladimir'

if __name__ == "__main__":
    inp = open("A-large.in")
    output = open("output.txt", 'w+')

    T = int(inp.readline())
    for i in range(0, T):
        x = int(inp.readline())
        base = x
        if x == 0:
            x = "INSOMNIA"
        else:
            d = dict()
            while True:
                for j in str(x):
                    d[j] = 1

                if len(d) == 10:
                    break
                else:
                    x += base

        output.write("Case #{0}: {1}\n".format(i + 1, x))

    inp.close()
    output.close()
