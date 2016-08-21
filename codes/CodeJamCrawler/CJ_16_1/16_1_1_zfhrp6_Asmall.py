from read import read
from Euler import primecheck


def calc(st):
    ret = ''
    for c in st:
        if ret == '':
            ret += c
        elif c >= ret[0]:
            ret = c + ret
        else:
            ret = ret + c
    return ret


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            S = it()
            ans = calc(S)
            outfile.write('Case #{}: {}\n'.format(caseidx, ans))
            print('Case #{}: {}'.format(caseidx, ans))


if __name__ == '__main__':
    main()
