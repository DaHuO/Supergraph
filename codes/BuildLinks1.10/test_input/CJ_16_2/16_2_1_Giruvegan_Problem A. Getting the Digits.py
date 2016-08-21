__author__ = 'Giruvegan'

def getting_digits(case_input):
    word_count = {}
    ans = []
    for letter in case_input:
        if letter in word_count:
            word_count[letter] += 1
        else:
            word_count[letter] = 1

    while 'Z' in word_count:
        word_count = decrease_and_check_remove(word_count, 'Z')
        word_count = decrease_and_check_remove(word_count, 'E')
        word_count = decrease_and_check_remove(word_count, 'R')
        word_count = decrease_and_check_remove(word_count, 'O')
        ans.append(0)

    while 'W' in word_count:
        word_count = decrease_and_check_remove(word_count, 'T')
        word_count = decrease_and_check_remove(word_count, 'W')
        word_count = decrease_and_check_remove(word_count, 'O')
        ans.append(2)

    while 'U' in word_count:
        word_count = decrease_and_check_remove(word_count, 'F')
        word_count = decrease_and_check_remove(word_count, 'O')
        word_count = decrease_and_check_remove(word_count, 'U')
        word_count = decrease_and_check_remove(word_count, 'R')
        ans.append(4)

    while 'R' in word_count:
        word_count = decrease_and_check_remove(word_count, 'T')
        word_count = decrease_and_check_remove(word_count, 'H')
        word_count = decrease_and_check_remove(word_count, 'R')
        word_count = decrease_and_check_remove(word_count, 'E')
        word_count = decrease_and_check_remove(word_count, 'E')
        ans.append(3)

    while 'X' in word_count:
        word_count = decrease_and_check_remove(word_count, 'S')
        word_count = decrease_and_check_remove(word_count, 'I')
        word_count = decrease_and_check_remove(word_count, 'X')
        ans.append(6)

    while 'S' in word_count:
        word_count = decrease_and_check_remove(word_count, 'S')
        word_count = decrease_and_check_remove(word_count, 'E')
        word_count = decrease_and_check_remove(word_count, 'V')
        word_count = decrease_and_check_remove(word_count, 'E')
        word_count = decrease_and_check_remove(word_count, 'N')
        ans.append(7)

    while 'O' in word_count:
        word_count = decrease_and_check_remove(word_count, 'O')
        word_count = decrease_and_check_remove(word_count, 'N')
        word_count = decrease_and_check_remove(word_count, 'E')
        ans.append(1)

    while 'F' in word_count:
        word_count = decrease_and_check_remove(word_count, 'F')
        word_count = decrease_and_check_remove(word_count, 'I')
        word_count = decrease_and_check_remove(word_count, 'V')
        word_count = decrease_and_check_remove(word_count, 'E')
        ans.append(5)

    while 'T' in word_count:
        word_count = decrease_and_check_remove(word_count, 'E')
        word_count = decrease_and_check_remove(word_count, 'I')
        word_count = decrease_and_check_remove(word_count, 'G')
        word_count = decrease_and_check_remove(word_count, 'H')
        word_count = decrease_and_check_remove(word_count, 'T')
        ans.append(8)

    while 'I' in word_count:
        word_count = decrease_and_check_remove(word_count, 'N')
        word_count = decrease_and_check_remove(word_count, 'I')
        word_count = decrease_and_check_remove(word_count, 'N')
        word_count = decrease_and_check_remove(word_count, 'E')
        ans.append(9)

    ans = map(str, sorted(ans))
    return ''.join(ans)

def decrease_and_check_remove(word_count, key):
    word_count[key] -= 1
    if word_count[key] == 0:
        word_count.pop(key)
    return word_count

if __name__ == '__main__':

    filepath = 'A-large.in.txt'
    fout = open(filepath.split('.')[0] + '.out.txt', 'w')
    all_input = open(filepath, 'r').readlines()
    case_num = int(all_input[0])
    for i in range(1, len(all_input)):
        case_input = all_input[i].replace('\n', '')
        fout.write('case #' + str(i) + ': ' + getting_digits(case_input) + '\n')