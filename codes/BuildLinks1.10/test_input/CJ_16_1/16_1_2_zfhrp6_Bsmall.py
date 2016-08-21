from read import read


def m2r(mat, idx):
    return mat[idx]


def m2c(mat, idx):
    ret = []
    for row in mat:
        ret.append(row[idx])
    return ret


def calc(mat, n):
    # mat1 = mat[:(n+1)/2]
    # mat2 = mat[(n-1)/2:]
    retd = {}
    for row in mat:
        for soldier in row:
            if soldier in retd:
                retd[soldier] += 1
            else:
                retd[soldier] = 1
    # print(retd)         #debuggggggggggggggggggggggggggggggggg
    return sorted([x[0] for x in filter(lambda x:x[1]%2, retd.items())])


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())   # case number

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            # input()                 #debugggggggggggggggggggggggggggg
            N = int(it())
            # print('N: {}'.format(N)) # debuggggggggggggggggggggggggggggg
            mat = []
            for _line in range(2*N - 1):
                row = map(int, it().split())
                mat.append(row)
            ans = calc(mat, N)
            outfile.write('Case #{}: {}\n'.format(caseidx, ' '.join(map(str, ans))))
            print('Case #{}: {}'.format(caseidx, ' '.join(map(str, ans))))


if __name__ == '__main__':
    main()
