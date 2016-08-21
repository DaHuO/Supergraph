__author__ = 'Arwin'
fn = 'B-large.in'
f = open(fn)
ansf = open("ans.txt", "w")

def rankfo(N, lists):
    matrix = [[None] * N] * N
    r = [0] * N
    c = [0] * N
    r[0] = 1
    lists.sort()
    matrix[0] = lists[0]
    for i in xrange(1, 2 * N - 1):
        if lists[i][0] in matrix[0]:  # insert to column
            idx = matrix[0].index(lists[i][0])
            if c[idx] == 0:
                for ii in xrange(1, N):
                    matrix[ii][idx] = lists[i][ii]
                c[idx] = 1
            else:  # insert row
                for ridx in xrange(1, N):  # find existing row start match
                    if matrix[ridx][0] == lists[i][0]:
                        break
                if matrix[ridx][0] != lists[i][0]:  # if no row start match
                    ridx = r.index(0)
                matrix[ridx] = lists[i]
                r[ridx] = 1
        else:  # insert row
            for ridx in xrange(1, N):  # find existing row start match
                if matrix[ridx][0] == lists[i][0]:
                    break
            if matrix[ridx][0] != lists[i][0]:  # if no row start match
                ridx = r.index(0)
            matrix[ridx] = lists[i]
            r[ridx] = 1
    if r.index(0):
        return matrix[r.index(0)]
    if c.index(0):
        idx= c.index(0)
        for ii in xrange(0, N):
            matrix[ii][idx] = lists[i][ii]

def rankf(N, lists):
    lists.sort()
    s= set()
    for i in xrange(0, 2 * N - 1):
        for num in lists[i]:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
    return sorted(s)

T= int(f.next())
for i in xrange(1,T+1):
    N= int(f.next())
    seq=[]
    for j in xrange(0, 2 * N - 1):
        seq.append(  map( int, f.next().strip().split() ) )
    ansf.write( 'Case #{0}: {1}\n'.format(i, ' '.join(map( str, rankf(N,seq))) ) )

ansf.close()