def solve(n, fout):
    d = set()
    it = n
    for i in range(1001):
        for j in str(it):
            d.add(j)
        if len(d) == 10:
            print(it, file=fout)
            return
        it += n
    print("INSOMNIA", file=fout)


def main():
    with open("input.txt") as fin, open("output.txt", 'w') as fout:
        T = int(fin.readline())
        for i in range(T):
            print("Case #{0}: ".format(i + 1), end='', file=fout)
            solve(int(fin.readline()), fout)
    
    
main()
    