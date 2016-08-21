__author__ = 'Giruvegan'


def flip_pancake(line):
    line_list = []
    for i in range(len(line)):
        if line[i] == '-':
            line_list.append(0)
        else:
            line_list.append(1)

    state = 0
    ext_num = 0
    while state == 0:
        start = line_list[0]
        for i in range(len(line_list)):
            if line_list[i] == start:
                if i == len(line_list)-1:
                    state=1
                continue
            else:
                flip_range(line_list, i)
                ext_num += 1
                break

    if line_list[0] == 0:
        flip_range(line_list, len(line_list))
        ext_num += 1

    return str(ext_num)


def flip_range(a_list, pos):
    for i in range(pos):
        a_list[i] = 1 - a_list[i]


if __name__ == '__main__':
    filepath = 'B-large.in.txt'
    fout = open(filepath.split('.')[0] + '.out.txt', 'w')
    all_input = open(filepath, 'r').readlines()
    case_num = int(all_input[0])
    for i in range(1, len(all_input)):
        case_input = all_input[i].replace('\n', '')
        print ('case #' + str(i) + ': ' + flip_pancake(case_input))
        fout.write('case #' + str(i) + ': ' + flip_pancake(case_input) + '\n')
