import fileinput

fin = fileinput.input()


def get_str(i, j, k, l):
    s = list("10000000000000000000000000000001")
    s[i] = '1'
    s[j] = '1'
    s[k] = '1'
    s[l] = '1'
    return ''.join(s)


def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        print("Case #{}:\n{} 3 4 5 6 7 8 9 10 11".format(case, get_str(0, 0, 0, 0)))
        counter = 1
        for i in range(15):
            for j in range(15):
                for k in range(i + 1, 15):
                    for l in range(j + 1, 15):
                        a = 2 * i + 1
                        b = 2 * j + 2
                        c = 2 * k + 1
                        d = 2 * l + 2
                        print("{} 3 4 5 6 7 8 9 10 11".format(get_str(a, b, c, d)))
                        counter += 1
                        if counter == 500:
                            return


if __name__ == '__main__':
    main()
