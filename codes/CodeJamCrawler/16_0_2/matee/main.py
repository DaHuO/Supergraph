def read_data():
    f = open('input.txt')
    number_of_testcases = int(f.readline())
    data_array = []
    for line in f:
        data_array.append([x for x in line.split()])
    if len(data_array) != number_of_testcases:
        print "Something is wrong with this file."
    return number_of_testcases, data_array


def are_all_happy(pancakes):
    for pancake in pancakes:
        if pancake == "-":
            return False
    return True


def flip_all(task):
    tmp = ''
    for item in task:
        if item == '-':
            tmp += '+'
        elif item == '+':
            tmp += '-'
    return tmp


def flip_around(task):
    return task[::-1]


def list2str(list):
    tmp = ""
    for item in str(list):
        if item == '+':
            tmp += '+'
        elif item == '-':
            tmp += '-'
    return tmp


def check_text_len(text, text_len):
    return len(text) < text_len


def checkpc(text, number_of_letter, round_number=0):
    round_number += 1
    if check_text_len(text, number_of_letter):
        return False, round_number

    number_to_change = max(find_longest(text), number_of_letter)
    tmp = flip_all_before_number(number_to_change, text)
    if are_all_happy(tmp):
        return True, round_number
    return checkpc(tmp, number_to_change + 1, round_number)


def find_longest(text):
    finding_char = text[0]
    the_same_sign = 0
    for item in text:
        if item == finding_char:
            the_same_sign += 1
        else:
            return the_same_sign
    return the_same_sign


def flip_all_before_number(number_of_letter, task_str):
    return flip_all(task_str[:number_of_letter]) + task_str[number_of_letter:]


def pancakes():
    numner_of_tc, data = read_data()
    print numner_of_tc
    f = open("output.txt",'w')
    for i, task in enumerate(data):
        task_str = list2str(task)
        min_number_of_round = 0
        for number_of_letter, pc in enumerate(task_str):
            if are_all_happy(task_str):
                break
            done, numberofround = checkpc(task_str, number_of_letter + 1)
            if done:
                if min_number_of_round > 0:
                    min_number_of_round = min(numberofround, min_number_of_round)
                else:
                    min_number_of_round = numberofround
        output = 'Case #%d: %d' % (i+1, min_number_of_round)
        print output
        f.write(output + '\n')
        f.close

if __name__ == '__main__':
    pancakes()
