


def Solution(i, N):
    if N == 0:
        print "Case #{}: {}".format(i, 'INSOMNIA')
        return 1
    pool = 0
    cnt = 1
    tmp = N * cnt
    while cnt < 100000:
        while tmp:
            b = tmp%10
            tmp/=10
            pool = pool | 1<<b
        if pool == 1023:
            print "Case #{}: {}".format(i, N*cnt)
            return 1
        cnt+=1
        tmp = N * cnt



if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        cnt = 1
        for i in xrange(int(line)):
            line = f.readline().strip('\n')
            out = Solution(cnt, int(line))
            cnt+=1