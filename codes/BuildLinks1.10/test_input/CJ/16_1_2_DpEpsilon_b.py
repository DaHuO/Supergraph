nodes = []
adj_matrix = []
cache = []
bt = []
n = 0
nd = 0

def dp(cur):
    if cache[cur] is None:
        cur_val = 0
        cur_bests = []
        for i in xrange(nd):
            if adj_matrix[cur][i]:
                v = dp(i)+1
                if v > cur_val:
                    cur_val = v
                    cur_bests = [i]
                if v == cur_val:
                    cur_bests = [i] + cur_bests
        if cur_bests:
            for cur_best in cur_bests:
                bt[cur].extend([cur] + backtrack for backtrack in bt[cur_best])
        else:
            bt[cur] = [[cur]]
        cache[cur] = cur_val
    return cache[cur]

def lt(a, b):
    return all([a[i] < b[i] for i in xrange(n)])

n_t = int(raw_input())
for t in xrange(1, n_t+1):
    n = int(raw_input())
    nd = 2*n-1
    cache = [None for i in xrange(nd)]
    bt = [[] for i in xrange(nd)]
    adj_matrix = [[None for j in xrange(nd)] for i in xrange(nd)]
    nodes = []
    for i in xrange(nd):
        nodes.append(tuple([int(x) for x in raw_input().split()]))

    for i in xrange(nd):
        for j in xrange(nd):
            adj_matrix[i][j] = lt(nodes[i], nodes[j])
    grid_nums_list = []
    for i in xrange(nd):
        chain_length = dp(i)
        if chain_length == n-1:
            grid_nums_list.extend(bt[i]) # SUCCESS
    assert(len(grid_nums_list) > 0) # FUCK

    for grid_nums in grid_nums_list:
        grid = [nodes[i] for i in grid_nums]
        set_grid_nums = set(grid_nums)
        set_rows = set([nodes[i] for i in xrange(nd) if i not in set_grid_nums])
        bad_rows = []
        for i in xrange(n):
            row = tuple([grid[j][i] for j in xrange(n)])
            if row not in set_rows:
                bad_rows.append(row)
        if len(bad_rows) == 1:
            print "Case #{0}: {1}".format(t, ' '.join([str(x) for x in bad_rows[0]]))
            break
    else:
        assert(False) # again, FUCK
