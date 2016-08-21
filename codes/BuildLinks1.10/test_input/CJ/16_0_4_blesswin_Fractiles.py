from math import sqrt
from itertools import count, islice

def main():
    T = int(input())
    for c in range(T):
        K, C, S = map(int, input().split())
        print("Case #{}: ".format(c + 1), end="")

        if S == K:
            for i in range(1, 1 + S):
                print("{} ".format(i), end="")
        elif 2 * S <= K:
            print("IMPOSSIBLE", end="");
        else:
            for i in range(2, 2 + S):
                print("{} ".format(i), end="")
        print()


if __name__ == '__main__':
    main()
