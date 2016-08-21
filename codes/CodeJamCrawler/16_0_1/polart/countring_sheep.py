def calc(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        numbers = set(range(10))
        i = 1
        while len(numbers) > 0:
            nn = str(n * i)
            i_numbers = set(map(int, nn))
            numbers -= i_numbers
            i += 1
        print 'I -- ', i - 1
        return nn


def main(file_name):
    in_filename = file_name + '.in'
    out_filename = file_name + '.out'
    with open(in_filename) as in_file, open(out_filename, 'w') as out_file:
        in_file.readline()
        for index, line in enumerate(in_file, start=1):
            n = int(line.strip())

            print '----------------'
            print 'N -- ', n
            ans = "Case #{}: {}\n".format(index, calc(n))
            out_file.write(ans)
            print ans


if __name__ == '__main__':
    # main('test')
    # main('small')
    main('large')
