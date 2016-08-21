

import os

OUTPUT_FILE_NAME = 'output_file.txt'
def ProblemA():
    input_file = open('input_file.txt', 'r')
    if(os.path.isfile(OUTPUT_FILE_NAME)):
        os.remove(OUTPUT_FILE_NAME)
    first = 0
    num_tests = 0
    test_number = 0
    for line in input_file:
        if(first == 0):
            num_tests = int(line)
            first = 1
        else:
            test_number = test_number + 1
            check_number(test_number, line.strip())
            if test_number == num_tests:
                print 'Done checking!!!'
                input_file.close()
                return 0
    print 'This should not happen'
    return -1


def check_number(test_case_number, S):
    output_file = open(OUTPUT_FILE_NAME, 'a')
    first = True
    text = ''
    Z_count = 0
    E_count = 0
    R_count = 0
    O_count = 0
    N_count = 0
    T_count = 0
    W_count = 0
    H_count = 0
    F_count = 0
    U_count = 0
    I_count = 0
    V_count = 0
    S_count = 0
    G_count = 0
    X_count = 0

    for idx in range(0,len(S)):
        if S[idx] == 'Z':
            Z_count += 1
        elif S[idx] == 'E':
            E_count += 1
        elif S[idx] == 'R':
            R_count += 1
        elif S[idx] == 'O':
            O_count += 1
        elif S[idx] == 'N':
            N_count += 1
        elif S[idx] == 'T':
            T_count += 1
        elif S[idx] == 'W':
            W_count += 1
        elif S[idx] == 'H':
            H_count += 1
        elif S[idx] == 'F':
            F_count += 1
        elif S[idx] == 'U':
            U_count += 1
        elif S[idx] == 'I':
            I_count += 1
        elif S[idx] == 'V':
            V_count += 1
        elif S[idx] == 'S':
            S_count += 1
        elif S[idx] == 'G':
            G_count += 1
        elif S[idx] == 'X':
            X_count += 1

    print S
    print text

    num_array = [0] * 10

    num_array[0] = Z_count
    E_count -= Z_count
    R_count -= Z_count
    O_count -= Z_count

    num_array[8] = G_count
    E_count -= G_count
    I_count -= G_count
    H_count -= G_count
    T_count -= G_count

    num_array[6] = X_count
    S_count -= X_count
    I_count -= X_count

    num_array[7] = S_count
    E_count -= S_count
    V_count -= S_count
    N_count -= S_count

    num_array[2] = W_count
    T_count -= W_count
    O_count -= W_count

    num_array[4] = U_count
    F_count -= U_count
    O_count -= U_count
    R_count -= U_count

    num_array[1] = O_count
    N_count -= O_count
    E_count -= O_count

    num_array[5] = V_count
    F_count -= V_count
    I_count -= V_count
    E_count -= V_count

    num_array[9] = I_count
    E_count -= I_count

    num_array[3] = H_count

    phonenum = ''
    for idx1,num in enumerate(num_array):
        for idx2 in range(0, num):
            phonenum = phonenum + str(idx1)


    print phonenum

    output_file.write('Case #' + str(test_case_number) + ': ' + phonenum + '\n')

    output_file.close()



if __name__ == "__main__":
    ProblemA()