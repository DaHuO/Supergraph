import random
from math import sqrt
import sys

sys.stdin = open('C-small-attempt0.in', 'r')
sys.stdout = open('C-small.out', 'w')

bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def factors(n, temp):
    #print(n)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            temp.append(str(i))
            yield i


def main():
    T = int(raw_input())
    N, J = raw_input().split(" ")
    temp = []
    print("Case #{}:".format(T))
    while len(temp) < int(J):
        retry = True
        while retry:
            nbr = "1"
            for i in range(int(N) - 2):
                nbr += str(random.randint(0, 1))
            nbr += "1"
            if nbr not in temp:
                f_cache = []
                for b in bases:
                    nb = int(nbr, base=b)
                    try:
                        _ = factors(nb, f_cache).next()
                    except StopIteration:
                        retry = True
                        break
                    else:
                        retry = False
                if not retry:
                    temp.append(nbr)
                    print("{} {}".format(
                        nbr, " ".join(f_cache)))


if __name__ == '__main__':
    main()