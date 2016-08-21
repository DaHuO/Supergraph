#!/usr/bin/env python


def choose_tiles(K, C, S):
    """For the small problem S=K so we can always just check the first K tiles."""
    if S < K:
        return 'IMPOSSIBLE'
    return str_arr(range(1, S+1))

def str_arr(arr):
    return ' '.join(map(str, arr))

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (i+1, choose_tiles(*map(int, raw_input().split())))

if __name__ == "__main__":
    main()
