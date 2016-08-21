import sys


def main():
    file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[1][:-2] + 'out', 'w')
    file.readline()  # throw away T
    for case, n in enumerate(map(int, file), start=1):
        seen = [False for _ in range(10)]
        m = 1
        num = 0
        if n != 0:
            while not all(seen):
                num = m * n
                for digit in str(num):
                    seen[int(digit)] = True
                m += 1
        out_file.write('Case #{}: {}\n'.format(
            case, num if num > 0 else 'INSOMNIA'))


if __name__ == '__main__':
    main()
