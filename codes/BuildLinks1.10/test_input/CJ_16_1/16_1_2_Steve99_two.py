def solve(grid):
    numbers = {}
    for i in grid:
        for j in i:
            if j in numbers:
                numbers[j] += 1
            else:
                numbers[j] = 1

    answer = []
    for i in numbers:
        if numbers[i] % 2 != 0:
            answer.append(int(i))
    answer.sort()
    answer = [str(i) for i in answer]
    answer = ' '.join(answer)

    return answer

cases = int(input())
grids = []

for _ in range(cases):
    n = int(input())
    grid = []
    for _ in range((n*2)-1):
        grid.append(input().split())
    grids.append(grid)

for i, grid in enumerate(grids):
    print("Case #{}: {}".format(i+1, solve(grid)))


