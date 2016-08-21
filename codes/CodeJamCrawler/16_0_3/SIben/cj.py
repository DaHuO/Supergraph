import math

global_results = []
global_values = []
cur_idx = 0

def parsing():
    nb_tests = int(raw_input())
    N = []
    J = []
    
    for _ in range(nb_tests):
        tmp_n, tmp_j = [int(i) for i in raw_input().split()]
        N.append(tmp_n)
        J.append(tmp_j)

    return nb_tests, N, J

def display(case_number):
    print "Case #" + str(case_number) + ": "
    for i in range(len(global_results)):
        print global_results[i] + ' ' + ' '.join(str(elem) for elem in global_values[i])

def is_valid(cur):
    global cur_idx
    array = []

    for i in range(2, 11):
        value = int(cur, i)
        for i in range(2, int(math.sqrt(value) + 1)):
            if value % i == 0:
                array.append(i)
                break

    if len(array) >= 9:
        global_values.append(array)
        cur_idx += 1
        global_results.append(cur)

def solve_for(N, J, cur):

    if len(global_results) >= J:
        return
        
    if N == 0:
        cur = '1' + cur + '1'
        is_valid(cur)
        return

    solve_for(N - 1, J, cur + '0')
    solve_for(N - 1, J, cur + '1')

def main():
    
    global global_results
    global global_values

    T, N, J = parsing()

    for i in range(T):
        global_results = []
        global_values = []
        solve_for(N[i] - 2, J[i], '')
        display(i + 1)


if __name__=='__main__':
    main()
