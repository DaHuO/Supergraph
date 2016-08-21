T = int(input())  # read a line with a single integer

result = []

def compute(rows, columns, nexts, noCheckIndex, inRow, N):
    if nexts == []:
        global result
        result = rows[:]
        return True
    if len(rows) + (1 if inRow else 0) > N or len(columns) + (1 if not inRow else 0) > N:
        return False
    nextOne = nexts[0]
    newNext = 1
    if inRow:
        for i, col in enumerate(columns):
            if i == noCheckIndex:
                continue
            if col[len(rows)] != nextOne[i]:
                return False
        rows.append(nextOne)
    elif len(columns) != noCheckIndex:
        for i, row in enumerate(rows):
            if row[len(columns)] != nextOne[i]:
                return False
        columns.append(nextOne)
    else:
        columns.append([])
        newNext = 0
    return compute(rows[:], columns[:], nexts[newNext:], noCheckIndex, True, N) or compute(rows[:], columns[:], nexts[newNext:], noCheckIndex, False, N)


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def myCmp(a, b):
    for i in range(len(a)):
        if (a[i] != b[i]):
            return a[i] - b[i]
    return 0

for case in range(1, T + 1):
        print("Case #{}:".format(case), end="")
        N = int(input())
        myLists = []
        for i in range(2 * N - 1):
            myLists.append([int(s) for s in input().split(" ")])
        myLists = sorted(myLists, key=cmp_to_key(myCmp))
        for i in range(N):
            if (compute([], [], myLists, i, True, N) or compute([], [], myLists, i, False, N)):
                for r in result:
                    print(" {}".format(r[i]), end="")
                break
        print("")

