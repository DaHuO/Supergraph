import fileinput
import collections

def compute(N):
    d = {}
    for i in range(1,200):
        for s in str(N * i):
            d[s] = 1
            if len(d) == 10:
                return str(N*i)
    return 'INSOMNIA'

if __name__ == "__main__":
    f = fileinput.input()
    T=int(f.readline())
    for line in range(1,T+1):
         N = [int(x) for x in f.readline().split()][0]
         print("Case #{0}: {1}".format(line, compute(N)))

