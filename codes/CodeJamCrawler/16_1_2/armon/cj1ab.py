from sys import argv


if __name__=='__main__':

    fin = open(argv[1], 'r')
    tnum = int(fin.readline())
    fout = open(argv[1]+'_out', 'w')

    for i in range(1, tnum+1):
        N = int(fin.readline())
        nums = set()
        for j in range(2*N-1):
            l = [int(n) for n in fin.readline().split()]
            for n in l:
                if n in nums:
                    nums.discard(n)
                else:
                    nums.add(n)
        fout.write('Case #{0}: {1}\n'.format(i, ' '.join([str(n) for n in sorted(nums)])))
