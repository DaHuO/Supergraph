import os
import sys


def main(in_file, out_file):
    with open(out_file, 'w') as wptr:
        with open(in_file, 'r') as rptr:
            lines = [lne.strip() for lne in rptr]
            t = int(lines[0])
            for i in range(1, t + 1):
                digits = set()
                n = int(lines[i])
                print n
                j = 1
                while len(digits) < 10 and n != 0:
                    x = j * n
                    print x
                    while x:
                        d = x % 10
                        digits.add(d)
                        x = x / 10
                    j += 1
                if len(digits) == 10:
                    ans = str(n * (j - 1))
                else:
                    ans = 'INSOMNIA'
                wptr.write('Case #' + str(i) + ': ' + ans + '\n')


if __name__ == '__main__':
    argv = sys.argv
    main(argv[1], argv[2])
