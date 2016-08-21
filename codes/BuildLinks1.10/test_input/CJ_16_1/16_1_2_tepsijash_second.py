import fileinput
from operator import itemgetter

fin = fileinput.input()

comp = []

def get_position(x):
    global comp
    to_ret = []
    for i in range(len(x)/2):
        if x[2*i][i] != x[2*i+1][i]:
            to_ret = i
            comp = x[2*i]
            x.insert(2*i, x[2*i])
        x[2*i+2:] = sorted(x[2*i+2:], key=itemgetter(i+1))
    if to_ret != []:
        return to_ret
    x.insert(len(x)-1, x[len(x)-1])
    comp = x[len(x)-1]
    return len(x[0])-1


def get_output(x, comp, pos):
    y = comp
    for i in range(len(comp)):
        if x[2*i][pos] == comp[i]:
            y[i] = x[2*i+1][pos]
        else:
            y[i] = x[2*i][pos]
    return y


def main():
    global comp
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        N = int(next(fin))
        x = []
        for t in range(2 * N - 1):
            x.append(map(int, next(fin).strip().split()))
        x = sorted(x)
        comp = []
        pos = get_position(x)
        print("Case #{}: {}".format(case, ' '.join(str(t) for t in get_output(x, comp, pos))))

if __name__ == '__main__':
    main()
