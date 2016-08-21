f_stub = 'B-small-attempt1'
f = open(f_stub + '.in', 'r')
o = open(f_stub + '.out', 'w')
import numpy as np
def row_or_col_given_assignment(assignment, vector1, vector2, i):
    for x in range(i):
        if assignment[x][i] == vector1[x] and assignment[x][i] != vector2[x]:
            return vector2, vector1 #row, col
        elif assignment[x][i] != vector1[x] and assignment[x][i] == vector2[x]:
            return vector1, vector2 #col, row
def check_success_condition(matrix, original_lists_c):
    failures, failure_lists = 0, []
    original_lists = list(original_lists_c)
    all_matrix = []
    for l in matrix.T:
        non_numpy_l = np.ndarray.tolist(l)
        all_matrix.append(non_numpy_l)
        if non_numpy_l not in original_lists:
            failures += 1
            failure_lists.append(l)
        else:
            original_lists.remove(non_numpy_l)
            continue
    for l in matrix:
        non_numpy_l = np.ndarray.tolist(l)
        all_matrix.append(non_numpy_l)
        if non_numpy_l not in original_lists:
            failures += 1
            failure_lists.append(non_numpy_l)
        else:
            original_lists.remove(non_numpy_l)
            continue
    if failures > 1:
        return False
    else:
        return failure_lists[0]
        # print(matrix)
        # print('orig list:', original_lists_c)
        # print(all_matrix)
        # print(failure_lists)
        # for elem in all_matrix:
        #     # print(elem)
        #     if elem not in original_lists_c:
        #         return elem
def attempt_placement(matrix, joined_lists, n, original_lists):
    if len(joined_lists) == 0:
        # print('assigned all:', matrix)
        success = check_success_condition(matrix, original_lists)
        # print('success:', success)
        if success is False:
            return False
        else:
            return success
    elif len(joined_lists[0]) == 1:
        case_copy1 = np.copy(matrix)
        case_copy1[:,n] = joined_lists[0][0]
        success = attempt_placement(case_copy1, joined_lists[1:], n+1, original_lists)
        if success is not False:
            return success
        case_copy2 = np.copy(matrix)
        case_copy2[n,:] = joined_lists[0][0]
        success = attempt_placement(case_copy2, joined_lists[1:], n+1, original_lists)        
        return success
    next_level = joined_lists[0]
    # print('next level:', next_level, len(joined_lists))
    p1 = np.copy(matrix)
    p1[:,n] = next_level[0]
    p1[n,:] = next_level[1]
    success = attempt_placement(p1, joined_lists[1:], n+1, original_lists)
    if success is not False:
        return success
    p2 = np.copy(matrix)
    p2[:,n] = next_level[1]
    p2[n,:] = next_level[0]
    success = attempt_placement(p2, joined_lists[1:], n+1, original_lists)
    return success

def find_missing_list(lists, n):
    # print(lists)
    resulting_matrix = np.zeros((n, n))
    i = 0
    joined_lists = []
    l_copy = list(lists)
    while i != n:
        index_firsts = {}
        cur_min = float('inf')
        for l in lists:
            if l[i] < cur_min:
                cur_min = l[i]
        n_th_same = [l for l in lists if l[i] == cur_min]
        for x in n_th_same:
            lists.remove(x)
        joined_lists.append(n_th_same)
        i += 1
    # print(l_copy)
    # print('joined', joined_lists)
    missing_list = attempt_placement(resulting_matrix, joined_lists, 0, l_copy)
    return missing_list
i = 1
n_cases = int(f.readline())
while i <= n_cases:
    n = int(f.readline())
    lists = []
    for _ in range((2*n) - 1):
        list_line = [int(x) for x in f.readline().split()]
        lists.append(list_line)
    missing_list = find_missing_list(lists, n)
    o.write('Case #' + str(i) + ': ' + ' '.join([str(int(x)) for x in missing_list]) + '\n')
    i += 1
f.close()
o.close()