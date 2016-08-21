r = 1

def main():
    mat = []
    testcase = int(input())
    for i in range(0, testcase):
        N = int(input())
        for j in range(0, 2 * N - 1):
            mat.append(str(input()))
        matrix(mat)
        mat = []


def matrix(mat):
    global r
    count = []
    ls = ' '.join(mat)
    ls = ls.split(" ")
    map(int, ls)
    for i in range(1, 2501):
        c = ls.count(str(i)) % 2
        if c is not 0:
            count.append(i)
    count.sort()
    out = ' '.join(str(e) for e in count)
    print("Case #{}: {}".format(r, out))
    r += 1


if __name__ == "__main__":
    main()
