MaxTimes = 1000


def alltrue(dict):
    for ele in dict:
        if not dict[ele]:
            return False
    return True


def function(N):
    judge = {i: False for i in range(10)}
    for i in xrange(1, MaxTimes):
        strN = str(i * N)
        for ele in judge:
            if judge[ele]:
                continue
            if strN.find(str(ele)) != -1:   # if contained, make judge'ele become true
                judge[ele] = True
        if alltrue(judge):
            return strN
    return 'INSOMNIA'


if __name__ == '__main__':
    with open('A-small-attempt0.in') as fin:
        T = int(fin.readline())
        for _ in range(T):
            N = int(fin.readline()[:-1])    # get input and change it to integer
            out = function(N)
            with open('out.txt', 'a') as fout:
                fout.write('Case #%d: %s\n' % (_ + 1, out))
