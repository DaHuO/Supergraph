def main():
    with open("fractiles.out", "w") as fout:
        with open("D-small-attempt0.in", "r") as fin:
            fin.readline()
            line = fin.readline()
            i = 1
            while line != "":
                (k, c, s) = line.split(" ")
                searches = get_searches(int(k), int(c))
                if len(searches) > int(s):
                    fout.write("Case #{0}: IMPOSSIBLE\n".format(i))
                else:
                    fout.write("Case #{0}:".format(i))
                    for tile in searches:
                        fout.write(" {0}".format(tile))
                    fout.write("\n")
                i += 1
                line = fin.readline()

def get_searches(k, c):
    if c == 1:
        return range(1, k+1)
    if k == 1:
        return [1]
    tile = 2
    tiles = []
    while tile <= k**c:
        tiles.append(tile)
        tile += 2*(k**(c-1)) + 2
    if k % 2 == 1:
        tiles.append(k**c)
    return tiles

    
if __name__=="__main__":
    main()
