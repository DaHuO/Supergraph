import os
import sys


def main(in_file, out_file):
    with open(out_file, 'w') as wptr:
        with open(in_file, 'r') as rptr:
            lines = [lne.strip() for lne in rptr]
            t = int(lines[0])
            for i in range(1, t + 1):
                S = lines[i]
                print S
                fg = 1
                ans = 0
                for j in range(1, len(S)+1):
                    print S[-j]
                    if fg and S[-j] == '-':
                        ans += 1
                        fg = 1 - fg
                    elif (not fg) and S[-j] == '+':
                        ans += 1
                        fg = 1 - fg
                wptr.write('Case #' + str(i) + ': ' + str(ans) + '\n')


if __name__ == '__main__':
    argv = sys.argv
    main(argv[1], argv[2])
