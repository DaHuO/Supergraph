"""
Determine whether original artwork was 'L' * k.
    - If possible, print set of tiles which must contain at least
      one 'G' if original was not 'L' * k.
    - If impossible (s too small to check your full set of tiles),
      print 'IMPOSSIBLE'.

Given k and c, if there were only one 'G' in the original, what are
all the locations where a 'G' could have ended up in the k ** c
artwork?

Small: S = K
Large: 1 <= S <= K
"""


def choose_tiles(k, c, s):
    # leftmost = 1
    # rightmost = k ** c
    section_len = k ** (c-1)
    total_len = k ** c
    # For the small input, just check the first element of each contiguous section.
    # Each section corresponds to a tile from the original, and we have enough
    # students to check each section since S = K -- that is, since we have one
    # student for every tile in the original.  If the tile in the original that
    # corresponds to a section were a 'G', then the section is guaranteed to begin
    # with 'G'.  'IMPOSSIBLE' won't be relevant in the small input.
    return range(1, total_len + 1, section_len)


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        K, C, S = map(int, raw_input().split())
        tiles = choose_tiles(K, C, S)
        answer = ' '.join(map(str, tiles)) if tiles else 'IMPOSSIBLE'
        print 'Case #{}: {}'.format(t, answer)


if __name__ == '__main__':
    main()
