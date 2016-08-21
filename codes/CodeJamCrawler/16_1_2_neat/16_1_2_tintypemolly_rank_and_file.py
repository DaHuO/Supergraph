import itertools
from copy import deepcopy


def main():
    with open('B-small-attempt0.in') as input_file, open('B-small-attempt0.out', 'w') as output_file:
        case_count = int(input_file.readline().strip())
        for i in xrange(case_count):
            case_no = i + 1
            N = int(input_file.readline().strip())
            rows = list()
            for j in xrange(2 * N - 1):
                row = [int(raw_data) for raw_data in input_file.readline().strip().split(' ')]
                rows.append(row)
            rows.sort(key=lambda row: row[0])

            for combination in itertools.combinations(rows, N):
                if not test_column_order(combination, N):
                    continue
                missing = get_missing_row(combination, rows, N)
                if missing:
                    missing = [str(el) for el in missing]
                    output_file.write('Case #%d: %s\n' % (case_no, ' '.join(missing)))
                    break


def test_column_order(rows, N):
    for i in xrange(N):
        column = [row[i] for row in rows]
        if not all([column[j] < column[j + 1] for j in xrange(N - 1)]):
            return False
    return True


def get_missing_row(rows, original_data, N):
    rows = list(rows)
    columns = [[row[i] for row in rows] for i in range(N)]
    check_list = deepcopy(original_data)
    for row in check_list:
        if row in rows:
            rows.remove(row)
        elif row in columns:
            columns.remove(row)
        else:
            return None
    if len(rows) + len(columns) != 1:
        return None
    else:
        return rows[0] if rows else columns[0]


if __name__ == '__main__':
    main()
