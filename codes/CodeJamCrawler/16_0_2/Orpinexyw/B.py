
def main():
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    T = int(fin.readline())
    for t in xrange(T):
        fout.write('Case #{}: '.format(t + 1))
        s = fin.readline().strip()
        if '-' not in s:
            fout.write('0\n')
            continue
        count = 0
        print len(s)
        for idx in xrange(len(s) - 1):
            if s[idx] != s[idx + 1]:
                count += 1
        if s[-1] != '+':
            count += 1
        fout.write('{}\n'.format(count))
    fout.close()



if __name__ == "__main__":
    main()