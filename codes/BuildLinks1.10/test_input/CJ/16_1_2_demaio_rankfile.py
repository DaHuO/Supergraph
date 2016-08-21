#! /usr/bin/python

import sys
from collections import defaultdict

def print_matrix(matrix, n):
    for i in range(n):
        row = [str(matrix[(i, j)]) + ", " for j in range(n)]
        print "".join(row)

def dfs(matrix, rows, val_to_idxs):
    if len(rows) == 0:
        return True
    row = rows[0]
    rows = rows[1:]
    start_num = row[0]
    idx_lists = list(val_to_idxs[start_num])
    for idx_list in idx_lists:
        works = True
        for i, idx in enumerate(idx_list):
            (low, high) = matrix[idx]
            if row[i] < low or row[i] > high:
                works = False
                break
        if works:
            old_feasibility = []
            for i, idx in enumerate(idx_list):
                (low, high) = matrix[idx]
                matrix[idx] = (max(low, row[i]), min(high, row[i]))
                old_feasibility.append((low, high))
            val_to_idxs[start_num].remove(idx_list)
            done = dfs(matrix, rows, val_to_idxs)
            if done:
                return True
            val_to_idxs[start_num].append(idx_list)
            for i, idx in enumerate(idx_list):
                matrix[idx] = old_feasibility[i]
    return False

def solve_conventional(matrix, top_rows, rows):
    # We have a top and left row, choose arbitrarily and do the DFS
    n = len(rows[0])
    low_val = min(row[0] for row in rows)
    hi_val = max(row[-1] for row in rows)
    for i in range(n):
        for j in range(n):
            matrix[(i, j)] = (low_val, hi_val)
    top_row = top_rows[0]
    left_col = top_rows[1]
    val_to_idxs = defaultdict(list)
    for i in range(n):
        row = [(j, i) for j in range(n)]
        if i > 0:
            val_to_idxs[left_col[i]] = [row]
        matrix[(0, i)] = (left_col[i], left_col[i])
    for j in range(n):
        col = [(j, i) for i in range(n)]
        if j > 0:
            val_to_idxs[top_row[j]].append(col)
        matrix[(j, 0)] = (top_row[j], top_row[j])
    
    rows = [row for row in rows if row not in top_rows]
    assert dfs(matrix, rows, val_to_idxs)
    # the only remaining idx_list should be the winner
    val_to_idxs = [idx_lists for start_num, idx_lists in val_to_idxs.iteritems() if len(idx_lists) > 0]
    assert len(val_to_idxs) == 1
    idx_list = val_to_idxs[0][0]
    sol = [matrix[idx][0] for idx in idx_list]
    return sol

def solve(lines, idx):
    n = int(lines[idx])
    rows = []
    for i in range(2 * n - 1):
        row_str = lines[idx+i+1]
        row = [int(c) for c in row_str.split(" ")]
        rows.append(row)
    
    sol = rows

    # mapping from (x, y) 0-indexed coordinate to (val, ref_count)
    matrix = dict()
    top_left = min(row[0] for row in rows)

    top_rows = [row for row in rows if row[0] == top_left]

    if len(top_rows) < 2:
        new_rows = []
        for row in rows:
            new_row = row[::-1]
            new_row = [-c for c in new_row]
            new_rows.append(new_row)
        top_left = min(row[0] for row in new_rows)
        top_rows = [row for row in new_rows if row[0] == top_left]
        sol = solve_conventional(matrix, top_rows, new_rows)
        sol = sol[::-1]
        sol = [-c for c in sol]
    else:
        sol = solve_conventional(matrix, top_rows, rows)
    return " ".join(str(s) for s in sol), 2 * n

def main():
    fn = sys.argv[1] 
    with open(fn) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    t = int(lines[0])
    idx = 1
    for i in range(t):
        result, num_used = solve(lines, idx)
        idx += num_used
        print "Case #%d: %s" % (i+1, result)

if __name__ == "__main__":
    main()
