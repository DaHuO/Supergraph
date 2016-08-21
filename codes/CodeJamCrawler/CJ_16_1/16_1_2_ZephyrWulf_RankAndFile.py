def fill(grid, obs, i, j, idx, N, skipped):

    if idx == 0:
        grid[0] = obs[0]
        return fill(grid, obs, 1, 0, 1, N, skipped)

    if idx == 2*N-1:
        return True

    # test if can be inserted in column j
    if j < N:
        possible = True
        for k in range(N):
            if grid[k][j] == -1:
                continue
            if grid[k][j] != obs[idx][k]:
                possible = False
                break
        if possible:
            resetCoord = []
            for k in range(N):
                if grid[k][j] == -1:
                    resetCoord.append([k,j])
                    grid[k][j] = obs[idx][k]
            if fill(grid, obs, i, j+1, idx+1, N, skipped):
                return True
            else:
                for c in resetCoord:
                    grid[c[0]][c[1]] = -1

    # test if can be inserted in row i
    if i < N:
        possible = True
        for k in range(N):
            if grid[i][k] == -1:
                continue
            if grid[i][k] != obs[idx][k]:
                possible = False
                break
        if possible:
            resetCoord = []
            for k in range(N):
                if grid[i][k] == -1:
                    resetCoord.append([i,k])
                    grid[i][k] = obs[idx][k]
            if fill(grid, obs, i+1, j, idx+1, N, skipped):
                return True
            else:
                for c in resetCoord:
                    grid[c[0]][c[1]] = -1

    if skipped:
        return False

    # test if can be inserted in column j
    if j+1 < N:
        possible = True
        for k in range(N):
            if grid[k][j+1] == -1:
                continue
            if grid[k][j+1] != obs[idx][k]:
                possible = False
                break
        if possible:
            resetCoord = []
            for k in range(N):
                if grid[k][j+1] == -1:
                    resetCoord.append([k,j+1])
                    grid[k][j+1] = obs[idx][k]
            if fill(grid, obs, i, j+2, idx+1, N, skipped):
                return True
            else:
                for c in resetCoord:
                    grid[c[0]][c[1]] = -1

    # test if can be inserted in row i + 1
    if i+1 < N:
        possible = True
        for k in range(N):
            if grid[i+1][k] == -1:
                continue
            if grid[i+1][k] != obs[idx][k]:
                possible = False
                break
        if possible:
            resetCoord = []
            for k in range(N):
                if grid[i+1][k] == -1:
                    resetCoord.append([i+1,k])
                    grid[i+1][k] = obs[idx][k]
            if fill(grid, obs, i+2, j, idx+1, N, True):
                return True
            else:
                for c in resetCoord:
                    grid[c[0]][c[1]] = -1

    return False

def rankAndFile(fin):
    N = int(fin.readline())
    obs = []
    for i in range(2*N-1):
        obs.append(map(int, fin.readline().split()))
    grid = [[-1]*N for _ in range(N)]

    obs.sort()

    fill(grid, obs, 0, 0, 0, N, False)

    for i in range(N):
        row = [grid[i][j] for j in range(N)]
        if row not in obs:
            return " ".join(map(str, row))
        else:
            obs.remove(row)
    for j in range(N):
        row = [grid[i][j] for i in range(N)]
        if row not in obs:
            return " ".join(map(str, row))
        else:
            obs.remove(row)


file = "small"
fin = open(file + ".in", 'r')
fout = open(file + ".out", 'w')

cases = int(fin.readline())

for i in range(cases):
    result = rankAndFile(fin)
    fout.write("Case #" + str(i+1) + ": " + str(result) + "\n")