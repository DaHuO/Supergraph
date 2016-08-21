import numpy as np


def test_row(mat, line, row):
    for i, v in enumerate(line):
        if mat[row, i] != 0 and mat[row, i] != v:
            return False
    return True


def test_col(mat, line, col):
    for i, v in enumerate(line):
        if mat[i, col] != 0 and mat[i, col] != v:
            return False
    return True


def write_row(mat, line, row):
    for i, v in enumerate(line):
        mat[row, i] = v


def write_col(mat, line, col):
    for i, v in enumerate(line):
        mat[i, col] = v


T = int(raw_input())
for case in range(T):
    N = int(raw_input())

    lines = []
    for i in range(2 * N - 1):
        values = map(int, raw_input().strip().split(' '))
        lines.append(values)

    db = {}
    missing = -1
    for i in range(N):
        lines.sort(key=lambda x: x[i], reverse=True)

        if len(lines) > 1 and lines[-1][i] == lines[-2][i]:
            l1, l2 = lines.pop(), lines.pop()
        else:
            l1, l2 = lines.pop(), None
            missing = i

        db[i] = (l1, l2)

    setup = False
    todo = range(N)
    mat = np.zeros(shape=(N, N), dtype=int)
    while todo:
        incomplete = []

        for i in todo:
            l1, l2 = db[i]

            if missing == i:
                if not test_row(mat, l1, i):
                    write_col(mat, l1, i)
                elif not test_col(mat, l1, i):
                    write_row(mat, l1, i)
                elif len(todo) > 1:
                    incomplete.append(i)
                else:
                    write_col(mat, l1, i)
                continue
            elif (mat == mat.T).all():
                write_row(mat, l1, i)
                write_col(mat, l2, i)
                setup = True
                continue

            if l1 == l2:
                write_col(mat, l1, i)
                write_row(mat, l2, i)
            elif not test_row(mat, l1, i):
                write_col(mat, l1, i)
                write_row(mat, l2, i)
            elif not test_col(mat, l1, i):
                write_row(mat, l1, i)
                write_col(mat, l2, i)
            elif not test_row(mat, l2, i):
                write_col(mat, l2, i)
                write_row(mat, l1, i)
            elif not test_col(mat, l2, i):
                write_row(mat, l2, i)
                write_col(mat, l1, i)
            else:
                incomplete.append(i)

        todo = incomplete

    test1 = tuple(mat[:, missing])
    test2 = tuple(mat[missing, :])

    current = tuple(db[missing][0])
    line = test1 if (current == test2) else test2
    answer = ' '.join(map(str, line))
    print "Case #{}: {}".format(case + 1, answer)
