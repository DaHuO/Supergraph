from copy import deepcopy
T = int(raw_input().strip())


def replace_mark(C, J, c__values, j__values):
    global min_value, min_c, min_j
    c_values = deepcopy(c__values)
    j_values = deepcopy(j__values)
    if len(c_values) != 0:
        c_index = c_values.pop()
        for i in range(10):
            replace_mark( C[:c_index] + str(i) + C[c_index+1:], J, c_values, j_values)
        # replace_mark( C[:c_index] + "0" + C[c_index+1:], J, c_values, j_values)
        # replace_mark( C[:c_index] + "9" + C[c_index+1:], J, c_values, j_values)
        # if J[c_index] != "?":
        #     replace_mark( C[:c_index] + J[c_index] + C[c_index+1:], J, c_values, j_values)
        #     int_j = int(J[c_index])
        #     if int_j > 1:
        #         replace_mark( C[:c_index] + str(int_j-1) + C[c_index+1:], J, c_values, j_values)
        #     if int_j < 8:
        #         replace_mark( C[:c_index] + str(int_j+1) + C[c_index+1:], J, c_values, j_values)
    elif len(j_values):
        j_index = j_values.pop()
        for i in range(10):
            replace_mark( C, J[:j_index] + str(i) + J[j_index+1:], c_values, j_values)
        # replace_mark( C, J[:j_index] + "0" + J[j_index+1:], c_values, j_values)
        # replace_mark( C, J[:j_index] + "9" + J[j_index+1:], c_values, j_values)
        # if C[j_index] != "?":
        #     replace_mark( C, J[:j_index] + C[j_index] + J[j_index+1:], c_values, j_values)
        #     int_c = int(C[j_index])
        #     if int_c > 1 :
        #         replace_mark( C, J[:j_index] + str(int_c-1) + J[j_index+1:], c_values, j_values)
        #     if int_c < 8:
        #         replace_mark( C, J[:j_index] + str(int_c+1) + J[j_index+1:], c_values, j_values)
    else:
        c = int(C)
        j = int(J)
        abs_diff = abs(c-j)
        if abs_diff < min_value or min_value == -1:
            min_value = abs_diff
            min_c = c
            min_j = j
        elif abs_diff == min_value:
            if c < min_c:
                min_value = abs_diff
                min_c = c
                min_j = j
            elif c == min_c:
                if j <= min_j:
                    min_value = abs_diff
                    min_c = c
                    min_j = j





for case in range(T):
    C, J = raw_input().strip().split()
    min_value = -1
    min_c = 0
    min_j = 0

    cc_values = []
    jj_values = []
    for char_index, char in enumerate(C):
        if char == "?":
            cc_values.append(char_index)
    for char_index, char in enumerate(J):
        if char == "?":
            jj_values.append(char_index)
    replace_mark(C, J, cc_values, jj_values)
    len_c = len(C)
    c_padding = len_c - len(str(min_c))
    j_padding = len_c - len(str(min_j))
    min_c = ("0" * c_padding) + str(min_c)
    min_j = ("0" * j_padding) + str(min_j)
    print "Case #{case}: {ans}".format(case=case+1, ans=min_c+ " "+min_j)