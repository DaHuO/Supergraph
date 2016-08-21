import sys


def main():
    inp = list()
    for line in sys.stdin:
        inp.append(int(line.replace('\n', '')))

    no_t = inp.pop(0)
    for i in range(no_t):
        N = inp[i]
        if N == 0:
            out_N = 'INSOMNIA'
        else:
            out_N = compute(N)
        print 'Case #%d:' % (i+1), out_N


def compute(N):
    ref_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    master_list = list()
    i = 1

    while(1):
        digit_list = [int(j) for j in str(i*N)]
        master_list = master_list + digit_list
        master_list = sorted(set(master_list))
        if master_list == ref_list:
            return i*N
        i += 1
        if i == 1000000000000:
            return 'INSOMNIA'
    return N

if __name__ == '__main__':
    main()
