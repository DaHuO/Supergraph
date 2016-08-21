import copy
import sys

def ok(a, b):
    if a is None or b is None:
        return False

    for x in xrange(len(a)):
        if a[x] and b[x] and a[x] != b[x]:
            return False
    return True

def get(grid, location, thing):
    if location >= len(grid):
        return None
    if thing == "row":
        return grid[location]
    else:
        answer = []
        for x in xrange(len(grid)):
            answer.append(grid[x][location])
        return answer

def add(grid, line, location, thing):
    if thing == "row":
        grid[location] = line
    elif thing == "column":
        for x in xrange(len(line)):
            grid[x][location] = line[x]

def verify(grid, data):
    # Rows
    no = 0
    for line in grid:
        if None in line:
            good = False
            for d in data:
                if ok(line, d):
                    good = True
                    break
            if not good:
                no = no + 1
                if no == 2:
                    return False
    for x in xrange(len(grid)):
        line = [grid[y][x] for y in xrange(len(grid))]
        if None in line:
            good = False
            for d in data:
                if ok(line, d):
                    good = True
                    break
            if not good:
                no = no + 1
                if no == 2:
                    return False

    return True

bad = None
value = None

C = set()

def recurse(grid, x, y, data):
    global bad
    global value

    if not data:
        value = grid
        if x < len(grid):
            bad = (x, "row")
        if y < len(grid):
            bad = (y, "column")
        return True

    if not verify(grid, data):
        return False

    store = copy.deepcopy(grid)
    current = data.pop()

    # First row
    check = get(grid, x, "row")
    if ok(current, check):
        add(grid, current, x, "row")
        if recurse(grid, x+1, y, data):
            return True

    # Second row
    if x+1 < N:
        grid = copy.deepcopy(store)
        check = get(grid, x+1, "row")
        if ok(current, check):
            add(grid, current, x+1, "row")
            if recurse(grid, x+2, y, data):
                bad = (x, "row")
                return True

    # First column
    grid = copy.deepcopy(store)
    check = get(grid, y, "column")
    if ok(current, check):
        add(grid, current, y, "column")
        if recurse(grid, x, y+1, data):
            return True

    # Second column
    if y+1 < N:
        grid = copy.deepcopy(store)
        check = get(grid, y+1, "column")
        if ok(current, check):
            add(grid, current, y+1, "column")
            if recurse(grid, x, y+2, data):
                bad = (y, "column")
                return True

    data.append(current)
    return False

def main(N, data):
    data = [d.split() for d in data]
    for x in xrange(len(data)):
        for y in xrange(len(data[0])):
            data[x][y] = int(data[x][y])
    data = sorted(data)[::-1]
    answer = [[None for _ in xrange(N)] for _ in xrange(N)]

    assert recurse(answer, 0, 0, data)

    return " ".join(map(str, get(value, bad[0], bad[1])))

T = int(raw_input())
for x in xrange(T):
    N = int(raw_input())
    lines = []

    for n in xrange(2*N - 1):
        lines.append(raw_input())
    print "Case #" + str(x + 1) + ": " + main(N, lines)
