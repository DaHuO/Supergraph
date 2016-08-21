import functools as ft
import operator as op
import collections as cl

def test(test_idx, N, data):
    lines = list(list(map(int, line.split(' ')))for line in sorted(data))
    chars = ft.reduce(op.add, lines)
    cou = cl.Counter(chars)
    lack = []
    for c, v in cou.items():
        if v % 2 != 0:
            lack.append(c)
    output = ' '.join(list(map(str, sorted(lack))))
    print("Case #{}: {}".format(test_idx, output))




def parse():
    N = int(input())
    data = []
    for _ in range(2*N-1):
        data.append(input())
    return N, data

def main():
    test_num = int(input())
    for test_idx in range(test_num):
        N, data = parse()
        test(test_idx+1, N, data)

if __name__ == '__main__':
    main()
