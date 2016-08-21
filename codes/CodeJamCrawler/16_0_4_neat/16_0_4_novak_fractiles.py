import sys

def find_tiles(k, c, s):
    if k == 1:
        return [1]

    if c == 1:
        if s < k:
            return []
        return range(1, k + 1)

    if s < k - 1:
        return []
    return range(2, k + 1)

def main():
    num_of_cases = int(raw_input())
    for i in xrange(1, num_of_cases + 1):
        k, c, s = [int(x) for x in raw_input().split(' ')]

        print 'Case #{}:'.format(i),

        tiles_to_check = find_tiles(k, c, s)
        if len(tiles_to_check) > 0:
            print ' '.join(str(x) for x in tiles_to_check)
        else:
            print 'IMPOSSIBLE'

if __name__ == '__main__':
    main()