import sys

def test():
    k, c, s = map(int, sys.stdin.readline().split())
    # TODO: Read a test case and return the answer to print

    if c == 1:
        return 'IMPOSSIBLE' if s < k else ' '.join(map(str, range(1, k + 1)))

    if k == c:
        return ' '.join(map(str, range(1, k + 1)))

    if k / 2 > s:
        return 'IMPOSSIBLE'

    tiles = []
    total_tiles = k ** c
    block_size = k ** (c - 1)
    for block in range(1, k + 1, 2):
        # Which tile in this block to look at?
        tile = (block - 1) * block_size + block + 1
        if tile > total_tiles:
            tile = total_tiles
        tiles.append(tile)
    return ' '.join(map(str, tiles))


def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)
