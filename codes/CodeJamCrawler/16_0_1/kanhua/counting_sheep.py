def count_sheep(N):

    if N==0:
        return "INSOMNIA"
    sheep = set()
    k = 0
    while len(sheep) < 10:
        k = k + 1
        last_N=N*k
        sheep |= set(str(last_N))

    return last_N


def test_small(max_N):

    for i in range(1,max_N,1):
        print(count_sheep(i))



def run_contest(in_file="test_micro.in",out_file="test_micro.out"):


    fp = open(in_file, 'r')
    op = open(out_file, 'w')
    N = int(fp.readline())

    for i in range(N):

        D = int(fp.readline())

        op.write("Case #%s: " % (i + 1))

        op.write(str(count_sheep(D)))

        op.write("\n")


if __name__=="__main__":
    #test_small(10000000)

    #print(count_sheep(1692))

    #run_contest(in_file="A-small-attempt0.in.txt",out_file="A-small-attempt0.out")

    run_contest(in_file="A-large.in.txt",out_file="A-large.out")