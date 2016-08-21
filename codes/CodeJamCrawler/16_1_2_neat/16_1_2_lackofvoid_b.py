import sys

def find_rows_cols(lists, firstrow):
    cols = [0,]*N
    
    ind = -1
    for j,el in enumerate(firstrow):
        found = -1
        for k,l in enumerate(lists):
            if el == l[0]:
                if found >= 0 and lists[found] != lists[k]:
                    found = -2
                elif found != -2:
                    found = k

        if found >= 0:
            cols[j] = lists.pop(found)

    rows = [firstrow,] + [0,]*(N-1)

    for I in range(100):
        for j in range(N):
            if rows[j] == 0:
                found = -1
                for m,pot in enumerate(lists):
                    isrow = True
                    for k,col in enumerate(cols):
                        # import pdb; pdb.set_trace()
                        if not (col == 0 or col[j] == pot[k]):
                            isrow = False
                    if isrow:
                        if found >= 0 and lists[found] != lists[m]:
                            found = -2
                        elif found != -2:
                            found = m
                if found >= 0:
                    rows[j] = lists.pop(found)


        for j in range(N):
            if cols[j] == 0:
                found = -1
                for m,pot in enumerate(lists):
                    isposs = True
                    for k,row in enumerate(rows):
                        if not (row == 0 or row[j] == pot[k]):
                            isposs = False
                    if isposs:
                        if found >= 0 and lists[found] != lists[m]:
                            found = -2
                        elif found != -2:
                            found = m
                if found >= 0:
                    cols[j] = lists.pop(found)
        if len(lists) == 0:
            break

    if len(lists) == 0:
        return rows, cols
    else:
        return None, None


fn = sys.argv[1]

with open(fn) as f:
    lines = f.read().splitlines() # removes trailing \n in each line

T = int(lines[0])
output = ""

lc = 1
for i in range(1,T+1):
    N = int(lines[lc])
    lc += 1
    lists = []
    for j in range(2*N-1):
        lists.append( [ int(el) for el in lines[lc].split(" ") ]  )
        lc += 1

    lists.sort(key=lambda l: l[0])
    orig_lists = list(lists)

    firstrow = lists.pop(0)
    rows, cols = find_rows_cols(lists, firstrow)
    if not rows:
        lists = list(orig_lists)
        firstrow = lists.pop(1)
        rows, cols = find_rows_cols(lists, firstrow)


    # print("rows:")
    # for r in rows:
        # print(r)
    # print("cols (post):")
    # for c in cols:
        # print(c)
    # print("lists:")
    # print(lists)

    assert len(lists)==0

    res = -1

    if 0 in rows:
        ind = rows.index(0)
        res = [ str(col[ind]) for col in cols ]
    elif 0 in cols:
        ind = cols.index(0)
        res = [ str(row[ind]) for row in rows ]

    assert res != -1

    print("Case #%i: %s" % (i, " ".join(res)))
