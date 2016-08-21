ans = None
def solve(L, N):
    global ans
    def search(following, k, rows, columns, missed):
        global ans
        # print('following', following)
        # print('k', k)
        # print('rows', rows)
        # print('columns', columns)
        # print('missed', missed)
        if k == N:
            ans = [L[x][missed] for x in rows]
            return
        N21 = 2 * N - 1
        valid_search = []
        if k == 0:
            possibles = range(N21)
        else:
            possibles = following[rows[-1]]
        for possible in possibles:
            if len(following[possible]) >= (N - k - 1):
                valid_search.append(possible)
        # print('valid_search', valid_search)
        for picked in valid_search:
            new_missed = missed
            filtered_columns = []
            ok = True
            for j in range(N):
                filtered_column = filter(lambda x: L[x][k] == L[picked][j] and x != picked, columns[j])
                # print('filtered_column', filtered_column)
                if not len(filtered_column):
                    if new_missed != -1 and new_missed != j:
                        ok = False
                        break
                    else:
                        new_missed = j
                filtered_columns.append(filtered_column)
            if ok:
                search(following, k + 1, rows + [picked], filtered_columns, new_missed)
                if ans: return

    N21 = 2 * N - 1
    following = [[] for _ in range(N21)]
    for i in range(N21):
        for j in range(N21):
            if i == j:
                continue
            ok = True
            for k in range(N):
                if L[j][k] <= L[i][k]:
                    ok = False
                    break
            if ok:
                following[i].append(j)
    columns = [range(N21) for _ in range(N21)]
    search(following, 0, [], columns, -1)
    return ' '.join(map(str, ans))

def main():
    global ans
    T = input()
    for i in xrange(1, T + 1):
        N = input()
        L = []
        for _ in range(2 * N - 1):
            l = map(int, raw_input().strip().split())
            L.append(l)
        ans = None
        print 'Case #{0}: {1}'.format(i, solve(L, N))

if __name__ == '__main__':
    main()
