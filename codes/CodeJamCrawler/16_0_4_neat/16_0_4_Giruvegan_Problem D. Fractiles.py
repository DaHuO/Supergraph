__author__ = 'Giruvegan'
import math

def comp_fractiles(case_input):
    K, C, S = map(int, case_input.split(' '))
    least_try = math.ceil(K/C)
    if S < least_try:
        return 'IMPOSSIBLE'
    ans = []
    pos = 0
    a_list = range(K)
    while pos+C < K:
        ans.append(str(list_to_baseK(a_list[pos: pos+C], K) + 1))
        pos = pos+C
    ans.append(str(list_to_baseK(a_list[pos: K], K) + 1))

    return ' '.join(ans)

def list_to_baseK(a_list, K):
    ans = 0
    for i in range(len(a_list)):
        ans += a_list[i]*K**i
    return ans

if __name__ == '__main__':
    filepath = 'D-small-attempt1.in.txt'
    fout = open(filepath.split('.')[0] + '.out.txt', 'w')
    all_input = open(filepath, 'r').readlines()
    case_num = int(all_input[0])
    for i in range(1, case_num+1):
        case_input = all_input[i].replace('\n', '')
        fout.write('case #' + str(i) + ': ' + comp_fractiles(case_input) + '\n')
