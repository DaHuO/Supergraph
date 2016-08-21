case_count = int(raw_input())
for case_number in xrange(1, case_count + 1):
    # S == K - simplifying for the "small" case
    k, c, _ = tuple(int(number) for number in raw_input().split())
    tiles_count = pow(k, c)
    clean_step = tiles_count / k
    tiles = range(1, tiles_count + 1, clean_step)

    print "Case #{}: {}".format(
        case_number,
        " ".join([str(tile) for tile in tiles])
    )
