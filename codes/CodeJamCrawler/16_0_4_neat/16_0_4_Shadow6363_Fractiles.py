import collections
import sys


def transform(sequence, C=1):
    K = len(sequence)
    old_seq = sequence[:]
    new_seq = sequence[:]

    for _ in xrange(1, C):
        new_seq = []
        for tile in old_seq:
            if tile == '1':
                new_seq.extend(sequence)
            else:
                new_seq.extend(['0']*K)
        old_seq = new_seq[:]

    return new_seq

def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        K,C,S = map(int, sys.stdin.readline().strip().split())

        '''
        bin_format = '{:>0'+str(K)+'}'
        lead_map = collections.defaultdict(set)

        originals = [bin_format.format(bin(num)[2:]) for num in xrange(0, pow(2, K))]
        for index, original in enumerate(originals):
            transformed = transform(list(original), C)
            for digit, tile in enumerate(transformed):
                if tile == '1':
                    lead_map[digit+1].add(index+1)
        '''

        clean = []
        for i in xrange(S):
            clean.append(str(((1+i) % (K**C))+1))

        print 'Case #{0}: {1}'.format(case+1, ' '.join(clean))


if __name__ == '__main__':
    main()
