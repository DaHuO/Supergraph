__author__ = 'Giruvegan'


def count_sheep(n):
    if int(n) == 0:
        return 'INSOMNIA'
    digits = set()
    x = 0
    while len(digits) < 10:
        x += int(n)
        for i in range(len(str(x))):
            digits.add(str(x)[i])
    return str(x)

if __name__ == '__main__':

    filepath = 'A-large.in.txt'
    fout = open(filepath.split('.')[0] + '.out.txt', 'w')
    all_input = open(filepath, 'r').readlines()
    case_num = int(all_input[0])
    for i in range(1, len(all_input)):
        case_input = all_input[i].replace('\n', '')
        print ('case #' + str(i) + ': ' + count_sheep(case_input))
        fout.write('case #' + str(i) + ': ' + count_sheep(case_input) + '\n')
