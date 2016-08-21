from read import read


def calc(k, c, s):
    '''
    k: original artwork size,
    c: complexity,
    s: num of allowable graduate students
    '''
    return list(range(1, k+1))


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            k, c, s = map(int, it().split())
            ans = calc(k, c, s)
            outfile.write('Case #{}: {}'.format(caseidx, ' '.join(map(str, ans))))
            outfile.write('\n')
            print('{} {} {} -> \n\tCase #{}: {}'.format(k, c, s, caseidx, ' '.join(map(str, ans))))


if __name__ == '__main__':
    main()
