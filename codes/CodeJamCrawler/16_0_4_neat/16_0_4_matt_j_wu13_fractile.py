import math

t = int(input())

def solve(K, C, S):
    if K == 1:
        return [1]
    minStudents = math.ceil(K / C)
    if S < minStudents:
        return ["IMPOSSIBLE"]
    ind = 0
    checkTiles = []
    curTile = 0
    exp = C - 1
    while ind < K:
        curTile += ind * (K ** exp)
        exp -= 1
        if exp < 0:
            checkTiles.append(curTile + 1)
            exp = C - 1
            curTile = 0
        ind += 1
    if curTile != 0:
        checkTiles.append(curTile + 1)
    return checkTiles


for i in range(1, t + 1):
    #Number of tiles in original
    #Complexity
    #Maximum number of tiles
    if i > 1:
        print()
    K, C, S = [int(s) for s in input().split(" ")]
    solution = solve(K, C, S)
    print("Case #" + str(i) + ":", end = "")
    for i in solution:
        print(" " + str(i), end = "")
