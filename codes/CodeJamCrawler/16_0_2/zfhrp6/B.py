from read import read

revd = {'-':'+', '+':'-'}

def calc(seq, cnt, mem = {}):
    tmpseq = seq.rstrip('+')
    # print(seq)
    if tmpseq in mem:
        mem[seq] = mem[tmpseq]
        return mem[seq]
    if tmpseq == '':
        mem[seq] = cnt
        return mem[seq]
    if set(tmpseq) == {'-'}:
        mem[seq] = cnt + 1
        return mem[seq]
    return calc(flip(tmpseq, tmpseq.index(revd[tmpseq[0]])), cnt+1, mem)


def calc2(seq, cnt, mem = {}):
    lc = 'x'
    cnt = 0
    seq = seq + '+'
    for c in seq:
        if lc == 'x':
            lc = c
            continue
        if c != lc:
            lc = c
            cnt += 1
    return cnt

def flip(seq, i):
    ret = ''
    for c in reversed(seq[:i]):
        ret += '+' if c == '-' else '-'
    for c in seq[i:]:
        ret += c
    return ret


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    mem = {}
    T = int(it())

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            inputline = it()
            ans = calc2(inputline, 0, mem)
            outfile.write('Case #{}: {}'.format(caseidx, ans))
            outfile.write('\n')
            print('{} -> Case #{}: {}'.format(inputline, caseidx, ans))


if __name__ == '__main__':
    main()
