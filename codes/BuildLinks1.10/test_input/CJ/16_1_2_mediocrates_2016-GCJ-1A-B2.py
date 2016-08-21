import collections

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    open(output_filename, 'wb').close()
    with open(input_filename, 'r+b') as f:
        with open(output_filename, 'r+b') as g:
            T = int(f.readline().strip())
            for i in range(1, T+1):
                N = int(f.readline().strip())
                lists = []
                for j in range(2*N-1):
                    lists.append(map(int, f.readline().strip().split()))
                a = collections.Counter(x for L in lists for x in L)
                b = [y for y in a if a[y]%2]
                print "Case #%d: %s" % (i, ' '.join(map(str, sorted(b))))
                g.write("Case #%d: %s\n" % (i, ' '.join(map(str, sorted(b)))))

if __name__ == '__main__':
    main()