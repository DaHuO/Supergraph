def solve_case(K, C, S):
    """
    Assuming K == S
    """
    tiles = range(0, K)
    for i in range(1, C):
        for tile_id in range(len(tiles)):
            tiles[tile_id] = tiles[tile_id] * K + tile_id
    for tile_id in range(len(tiles)):
        tiles[tile_id] += 1
    return " ".join(map(str, tiles))

f = open("D-small-attempt0.in", "r")
g = open("D-small-attempt0.out", "w")

num_test_cases = int(f.readline())
for case_no in range(1, num_test_cases + 1):
    print case_no
    (K, C, S) = map(int, f.readline().split())
    g.write("Case #" + str(case_no) + ": " + solve_case(K, C, S) + "\n")
    #print K, C, S, solve_case(K, C, S)
g.close()
