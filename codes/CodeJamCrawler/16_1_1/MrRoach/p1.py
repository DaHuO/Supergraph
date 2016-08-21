def solve(w):
    lastWord = ''
    for c in w:
        if c + lastWord > lastWord + c:
            lastWord = c + lastWord
        else:
            lastWord = lastWord + c
    return lastWord

if __name__ == '__main__':
    fin = open('A-large.in', 'r')
    fout = open('out.txt', 'w+')
    n = int(fin.readline())
    for i in range(n):
        w = fin.readline().strip()
        fout.write("Case #{0}: {1}\n".format(i + 1, solve(w)))
    fin.close()
    fout.flush()
    fout.close()
