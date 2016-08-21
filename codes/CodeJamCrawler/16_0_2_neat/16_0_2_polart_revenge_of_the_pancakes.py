from itertools import groupby


def calc(s):
    s = [1 if c == '+' else 0 for c in s]
    return len(list(groupby(s))) - 1 + int(not s[-1])


def main(file_name):
    in_filename = file_name + '.in'
    out_filename = file_name + '.out'
    with open(in_filename) as in_file, open(out_filename, 'w') as out_file:
        in_file.readline()
        for index, line in enumerate(in_file, start=1):
            s = line.strip()

            print '----------------'
            print 'S -- ', s
            ans = "Case #{}: {}\n".format(index, calc(s))
            out_file.write(ans)
            print ans


if __name__ == '__main__':
    # main('test')
    # main('small')
    main('large')
