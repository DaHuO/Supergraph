def rank_and_file(n, lines):
    lines = list(map(tuple, lines))
    groups = []
    start = 0
    for i in range(n):
        lines[start:] = sorted(lines[start:], key=lambda x: x[i])
        if start==2*n-1-1 or lines[start][i] < lines[start+1][i]:
            groups.append([lines[start]])
            start += 1
            missing_index = i
        else:
            groups.append([lines[start], lines[start+1]])
            start += 2
    res = []
    for i in range(n):
        if i == missing_index:
            res.append(groups[i][0][i])
        else:
            xs = [x[missing_index] for x in groups[i]]
            x = groups[missing_index][0][i]
            if x == xs[0]:
                res.append(xs[1])
            else:
                assert xs[1] == x
                res.append(xs[0])
    return res


def run(infile_name):
    outfile_name = infile_name+'.out'
    with open(outfile_name, 'w') as outfile, open(infile_name) as infile:
        T = int(infile.readline())
        for t in range(T):
            N = int(infile.readline())
            lines = []
            for i in range(2*N-1):
                lines.append(tuple(map(int, infile.readline().strip().split())))
            res = rank_and_file(N, lines)
            outfile.write('Case #{}: {}\n'.format(t+1, ' '.join(map(str, res))))

if __name__ == '__main__':
    import sys
    infile_name = sys.argv[1]
    run(infile_name)
