def solve(n, a):
    troop = [[0] * n for i in range(n)]
    minH = min(line[0] for line in a)
    usedLines = [False] * len(a)
    firstHorizontalFilled = False
    firstVerticalFilled = False
    count = 0
    for line in a:
        if line[0] == minH:
            if firstHorizontalFilled:
                for i in range(n):
                    troop[i][0] = line[i]
                firstVerticalFilled = True
            else:
                troop[0] = line
                firstHorizontalFilled = True
            usedLines[count] = True
        count += 1
    if not firstHorizontalFilled or not firstVerticalFilled:
        b = [[-x for x in line][::-1] for line in a[::-1]]
        res = solve(n, b)
        res = [-x for x in res][::-1]
        return res
    dupLines = []
    count = 0
    for line in a:
        if not usedLines[count] and a.count(line) > 1:
            dupLines += [line]
            usedLines[count] = True
        count += 1
    for line in dupLines:
        ind = troop[0].index(line[0])
        troop[ind] = line
        for i in range(n):
            troop[i][ind] = line[i]
    record = [a[i] for i in range(2 * n - 1) if not usedLines[i]]
    result = search(troop, record, 0, n)
    correctRecord = [line for line in result]
    for index in range(n):
        vertical = [result[i][index] for i in range(n)]
        correctRecord += [vertical]
    usedLines = [False] * len(a)
    for line in correctRecord:
        count = 0
        found = False
        for target in a:
            if not usedLines[count] and target == line:
                usedLines[count] = True
                found = True
                break
            count += 1
        if not found:
            return line
        count += 1
    return None    

def search(troop, record, index, n):
    if index == len(record):
        return troop
    line = record[index]
    # Put vertically
    if line[0] in troop[0]:
        ind = troop[0].index(line[0])
        match = True
        for i in range(n):
            if troop[i][ind] not in (0, line[i]):
                match = False
                break
        if match:
            tempLine = [troop[i][ind] for i in range(n)]
            for i in range(n):
                troop[i][ind] = line[i]
            ret = search(troop, record, index + 1, n)
            if ret is not None:
                return ret
            for i in range(n):
                troop[i][ind] = tempLine[i]

    # Put horizontally
    vertFirst = [troop[i][0] for i in range(n)]
    if line[0] in vertFirst:
        ind = vertFirst.index(line[0])
        match = True
        for i in range(n):
            if troop[ind][i] not in (0, line[i]):
                match = False
                break
        if match:
            tempLine = [troop[ind][i] for i in range(n)]
            for i in range(n):
                troop[ind][i] = line[i]
            ret = search(troop, record, index + 1, n)
            if ret is not None:
                return ret
            for i in range(n):
                troop[ind][i] = tempLine[i]
    return None

if __name__ == '__main__':
    fin = open('B-small-attempt1.in', 'r')
    fout = open('out.txt', 'w+')
    T = int(fin.readline())
    for i in range(T):
        N = int(fin.readline())
        a = []
        for j in range(2 * N - 1):
            line = [int(num) for num in fin.readline().strip().split()]
            a += [line]
        res = solve(N, a)
        res = [str(x) for x in res]
        fout.write("Case #{0}: {1}\n".format(i + 1, ' '.join(res)))
    fin.close()
    fout.flush()
    fout.close()
