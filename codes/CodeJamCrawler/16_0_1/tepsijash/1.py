import fileinput
from math import floor

fin = fileinput.input()


def find_N(x):
    digits = [0 for i in range(10)]
    if x == 0:
        return "INSOMNIA"

    counter = 0
    m = x
    while counter < 10:
        t = int(m)
        while t > 0:
            if digits[t % 10] == 0:
                digits[t % 10] = 1
                counter = counter + 1
            t = int(floor(t / 10))
        m = m + x

    return m - x


def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        x = int(next(fin))
        N = find_N(x)
        print("Case #{}: {}".format(case, N))

if __name__ == '__main__':
    main()
