def solve(p):
    K, C, S = [int(i) for i in p.split()]
    return ' '.join(str(i) for i in range(1, K+1))


def main():
    f_in = open('D-small-attempt0.in', 'r')
    # f_in = open('D-small-test.in', 'r')
    f_out = open('D-small.out', 'w')
    n = int(f_in.readline())
    for i in range(n):
        p = f_in.readline()
        s = "Case #{}: {}\n".format(i+1, solve(p.strip()))
        print s
        f_out.write(s)
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
