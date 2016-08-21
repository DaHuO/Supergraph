from math import pow

def parsing():
    nb_tests = long(raw_input())
    K = []
    C = []
    S = []
    
    for _ in range(nb_tests):
        t_k, t_c, t_s = [long(i) for i in raw_input().split()]
        K.append(t_k)
        C.append(t_c)
        S.append(t_s)

    return nb_tests, K, C, S

def display(case_number, result):
    print "Case #" + str(case_number) + ": " + ' '.join([str(i) for i in result])

def solve_for(K, C, S):

    return range(1, K + 1)

def main():
    
    nb_tests, K, C, S = parsing()
    result = []

    for i in range(nb_tests):
        if S[i] < long(K[i] / 2) or C[i] == 1 and S[i] < K[i]:
            result.append([])
            result[i].append(-1)
        elif C[i] == 1:
            result.append([i + 1 for i in range(K[i])])
        else:
            result.append(solve_for(K[i], C[i], S[i]))

    for i in range(nb_tests):
        if result[i][0] == -1:
            print "Case #" + str(i + 1) + ": IMPOSSIBLE"
        else:
            display(i + 1, result[i])

if __name__=='__main__':
    main()
