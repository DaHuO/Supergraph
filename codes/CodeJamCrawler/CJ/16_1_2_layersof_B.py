DEBUG=0

def main():
    T = input()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())

def solve():
    N = input()
    lists = []
    for i in range(2*N-1):
        lists.append(map(int, raw_input().split()))
    lists.sort()
    # print lists

    rows = [lists[0]] + [None for i in range(N-1)]
    cols = [None for i in range(N)]

    return ' '.join(map(str, rec(N, lists[1:], rows, cols)))


def rec(N, lists, rows, cols, depth=0):
    if DEBUG: print_board(N, rows, cols, depth)
    if not lists:
        return search_result(rows, cols)
    for ind in find_valid_row_inds(N, rows, cols, lists[0]):
        if rows[ind]: continue
        result = rec(N, lists[1:], rows[:ind] + [lists[0]] + rows[ind+1:], cols, depth+1)
        if result: return result
    else:
        for ind in find_valid_col_inds(N, rows, cols, lists[0]):
            if cols[ind]: continue
            result = rec(N, lists[1:], rows, cols[:ind] + [lists[0]] + cols[ind+1:], depth+1)
            if result: return result
        else:
            return None



def row_valid(N, rows, cols, n, row):
    for i, (r, col) in enumerate(zip(row, cols)):
        if col:
            if col[n] != r:
                return False
    for i in range(n-1, -1, -1):
        if rows[i]:
            for j in range(N):
                if rows[i][j] >= row[j]:
                    if DEBUG: print 'invalid row', n, row
                    return False
            else:
                break
    for i in range(n, N):
        if rows[i]:
            for j in range(N):
                if rows[i][j] <= row[j]:
                    if DEBUG: print 'invalid row2', n, row
                    return False
            else:
                break
    return True
    
def col_valid(N, rows, cols, n, col):
    for i, (c, row) in enumerate(zip(col, rows)):
        if row:
            if row[n] != c:
                return False
    for i in range(n-1, -1, -1):
        if cols[i]:
            for j in range(N):
                if cols[i][j] >= col[j]:
                    if DEBUG: print 'invalid col', n, col
                    return False
            else:
                break
    for i in range(n, N):
        if cols[i]:
            for j in range(N):
                if cols[i][j] <= col[j]:
                    if DEBUG: print 'invalid col2', n, col
                    return False
            else:
                break
    return True
    
def find_valid_col_inds(N, rows, cols, row):
    inds = []
    for i in range(N):
        if col_valid(N, rows, cols, i, row):
            inds.append(i)
    return inds


def find_valid_row_inds(N, rows, cols, col):
    inds = []
    for i in range(N):
        if row_valid(N, rows, cols, i, col):
            inds.append(i)
    return inds

def search_result(rows, cols):
    if None in cols:
        return search_result(cols, rows)
    ind = rows.index(None)

    return [col[ind] for col in cols]


def print_board(N, rows, cols, indent=0):
    grid = [[None for i in range(N)] for j in range(N)]

    for i in range(N):
        if rows[i]:
            grid[i] = rows[i][:]
        else:
            for j in range(N):
                if cols[j]:
                    grid[i][j] = cols[j][i]
    print ' ',
    print ' ' * indent,
    for j in range(N):
        if cols[j]:
            print '   v',
        else:
            print '    ',
    print
    for i in range(N):
        print ' ' * indent,
        print '>' if rows[i] else ' ',
        for j in range(N):
            if grid[i][j]:
                print '%4d' % grid[i][j],
            else:
                print '   _',
        print
            

if __name__ == '__main__':
    main()
