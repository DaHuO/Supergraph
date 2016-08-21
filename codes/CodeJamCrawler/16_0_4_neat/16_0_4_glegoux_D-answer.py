#!/usr/bin/env python3

# assume S = K
def get_tiles_to_clean(K, C, S):
    if S < K:
        return "IMPOSSIBLE"
    tiles = []
    for k in range(1,S+1):
        tiles.append(k*(K**(C-1)))
    return tiles

def print_answer(n, result):
    res = ""
    if type(result) in [list, tuple]:
        res = " ".join(map(str, result))
    elif type(result) == int:
        res = str(result)
    elif type(result) == str:
        res = result
    print("Case #{}: {}".format(n, res))

def main():
    T = int(input())
    for t in range(T):
        K, C, S = list(map(int, input().split(' ')))
        print_answer(t + 1, get_tiles_to_clean(K, C, S))

if __name__ == "__main__":
    main()
