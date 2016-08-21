
from collections import Counter

def main():

    #f = open('B-small-attempt1.in', 'r')
    f = open('B-large.in', 'r')
    fout = open('b.out', 'w')

    T = int(f.readline())

    t = 1
    while t <= T:
        n = int(f.readline().strip())
        counter = Counter()

        for i in xrange(0, 2*n-1):
            num_list = f.readline().split()
            counter.update(num_list)

        result = []
        for k in counter.iterkeys():
            if counter[k] % 2:
                result.append(int(k))

        result.sort()
        fout.write('Case #%d: %s\n' % (t, " ".join(str(x) for x in result)))

        t += 1

    f.close()
    fout.close()

if __name__ == '__main__':
    main()
