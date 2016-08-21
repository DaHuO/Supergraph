import fileinput

fin = fileinput.input()


def get_Max(x):
    y = [x[0]]
    for i in range(1, len(x)):
        if ord(x[i]) >= ord(y[0]):
            y = [x[i]] + y
        else:
            y = y + [x[i]]
    return ''.join(y)


def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        x = next(fin).strip()
        y = get_Max(x)
        print("Case #{}: {}".format(case, y))

if __name__ == '__main__':
    main()
