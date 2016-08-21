T = int(input())

solr = []

def evrows(rs):
    global rows
    global N
    global solr

    rem = rows.copy()
    #print("rem", rem)
    #print("rs", rs)

    for row in rs:
        #print("row", row)
        rem.remove(row)
        #print("removed", row)

    nomatch = 0
    for c in range(N):
        col = []
        for r in range(N):
            col.append(rs[r][c])
        if col not in rem:
            nomatch += 1
            solr = col

    if nomatch == 1:
        return True


def filt(row, remrows):
    frs = []
    for r in remrows:
        good = True
        for i,v in enumerate(r):
            if v <= row[i]:
                good = False
                break

        if good:
            frs.append(r)

    return frs

def rec(rs, remrs, n):
    if n == N:
        return evrows(rs)

    for row in remrs:
        fr = filt(row, remrs)
        if rec(rs + [row], fr, n+1):
            return True

for t in range(T):

    N = int(input())

    rows = []
    for i in range(2*N - 1):
        row = list(map(int, input().strip().split(' ')))
        rows.append(row)

    for row in rows:
        fr = filt(row, rows)
        if rec([row], fr, 1):
            break

    solstr = ' '.join(map(str, solr))

    print("Case #" + str(t+1) + ": " + solstr)
