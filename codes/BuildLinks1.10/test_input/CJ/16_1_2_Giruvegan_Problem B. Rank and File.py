__author__ = 'Giruvegan'
from collections import defaultdict

def rankFile(N, case_input):
    num_dict = defaultdict(int)
    ans = []
    for line in case_input:
        line = line.replace('\n', '').split(' ')
        for num in line:
            num_dict[num] += 1
    for k, v in num_dict.items():
        if v%2 != 0:
            ans.append(int(k))
    ans = map(str, sorted(ans))
    return ' '.join(ans)


if __name__ == '__main__':

    filepath = 'B-large.in.txt'
    fout = open(filepath.split('.')[0] + '.out.txt', 'w')
    all_input = open(filepath, 'r').readlines()
    case_num = int(all_input[0])
    case_no = 1
    pos = 1
    while pos < len(all_input):
        N = int(all_input[pos].replace('\n', ''))
        case_input = all_input[pos+1: pos+2*N]
        fout.write('case #' + str(case_no) + ': ' + rankFile(N, case_input) + '\n')
        pos = pos + 2*N
        case_no += 1