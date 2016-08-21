"""
Google qualification round, Fractiles

@author: Faegheh Hasibi
"""


def fractiles(k, c, s):
    """Solves Fractiles problem"""
    if s < k:
        return "IMPOSSIBLE"
    tiles = []
    for i in range(1, k+1):
        tiles.append(i * (k ** (c - 1)))
    return " ".join(str(tile) for tile in tiles)


def main():
    # print(fractiles(2, 3, 2))
    t = int(input())
    for i in range(1, t + 1):
        k, c, s = [int(s) for s in input().strip().split(" ")]
        print("Case #{}: {}".format(i, fractiles(k, c, s)))

if __name__ == "__main__":
    main()