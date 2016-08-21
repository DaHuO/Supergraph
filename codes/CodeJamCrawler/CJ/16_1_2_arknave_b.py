from collections import Counter

def insert_row(grid, x, r):
    #print("Inserting", r, "at row", x)
    for i in range(len(r)):
        grid[x][i] = r[i]

def insert_col(grid, x, c):
    #print("Inserting", c, "at col", x)
    for i in range(len(c)):
        grid[i][x] = c[i]

def valid_row(grid, x, r):
    if all([v == 0 for v in grid[x]]):
            return False
    for i in range(len(r)):
        if grid[x][i] != 0 and grid[x][i] != r[i]:
            return False
    return True

def valid_col(grid, x, c):
    non_zero = False
    for i in range(len(c)):
        if grid[i][x] != 0:
            non_zero = True
            if grid[i][x] != c[i]:
                return False
    return non_zero

def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

def extract(grid):
    out = []
    for row in grid:
        out.append(row[:])
    N = len(grid)
    for j in range(N):
        col = []
        for i in range(N):
            col.append(grid[i][j])
        out.append(col)
    return out

def main():
    T = int(input())
    for case_num in range(1, T + 1):
        N = int(input())
        opts = []
        for _ in range(2 * N - 1):
            opts.append([int(x) for x in input().split()])

        opts.sort()
        grid = [[0 for _ in range(N)] for _ in range(N)]
        used_row = [False] * N
        used_col = [False] * N

        insert_row(grid, 0, opts[0])
        used_row[0] = True
        skip = False

        cands = opts[1:]
        x = 1

        while len(cands) > 0:
            next_cands = []
            for cand in cands:
                score = 0
                enc_i = -1
                for i in range(N):
                    if not used_row[i] and valid_row(grid, i, cand):
                        score += 1
                        enc_i = i
                    if not used_col[i] and valid_col(grid, i, cand):
                        score += 1
                        enc_i = -1 * i
                if 0 < score <= x:
                    if enc_i > 0:
                        insert_row(grid, enc_i, cand)
                        used_row[enc_i] = True
                    else:
                        insert_col(grid, -1 * enc_i, cand)
                        used_col[-1 * enc_i] = True
                else:
                    next_cands.append(cand)

            cands = next_cands
            x += 1

        source = Counter(map(tuple, extract(grid)))
        given = Counter(map(tuple, opts))

        ans = map(str, list(list((source - given).items())[0][0]))

        #print(opts)
        print("Case #{0}: {1}".format(case_num, ' '.join(ans)))#' '.join([str(x) for x in ans])))

main()
