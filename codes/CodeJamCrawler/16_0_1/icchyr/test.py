
def search(n):
    if n is 0:
        return "INSOMNIA"
    N = n
    dset = set()
    count = 0
    while len(dset) != 10:
        [dset.add(c) for c in str(N)]
        count += 1
        N += n

    return N - n

if __name__ == '__main__':
    N = input()
    for i in range(N):
        print "Case #{0}:".format(i+1), search(input())
