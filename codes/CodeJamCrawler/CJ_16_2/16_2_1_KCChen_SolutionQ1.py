question_numbers = int(raw_input())
from collections import defaultdict
for question_id in xrange(0, question_numbers):
    task = list(raw_input())
    alpha_dict=defaultdict(int)

    K=list('EFGHINORSTUVWXZ')
    for k in K:
        alpha_dict[k]

    for i in range(0, len(task)):
        for key in alpha_dict:
            if task[i] == key:
                alpha_dict[key] += 1
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # zero
    numbers[0] = alpha_dict['Z']
    alpha_dict['Z'] -= numbers[0]
    alpha_dict['E'] -= numbers[0]
    alpha_dict['R'] -= numbers[0]
    alpha_dict['O'] -= numbers[0]

    # two
    numbers[2] = alpha_dict['W']
    alpha_dict['T'] -= numbers[2]
    alpha_dict['W'] -= numbers[2]
    alpha_dict['O'] -= numbers[2]

    # four
    numbers[4] = alpha_dict['U']
    alpha_dict['F'] -= numbers[4]
    alpha_dict['O'] -= numbers[4]
    alpha_dict['U'] -= numbers[4]
    alpha_dict['R'] -= numbers[4]

    # six
    numbers[6] = alpha_dict['X']
    alpha_dict['S'] -= numbers[6]
    alpha_dict['I'] -= numbers[6]
    alpha_dict['X'] -= numbers[6]

    # five
    numbers[5] = alpha_dict['F']
    alpha_dict['F'] -= numbers[5]
    alpha_dict['I'] -= numbers[5]
    alpha_dict['V'] -= numbers[5]
    alpha_dict['E'] -= numbers[5]

    # eight
    numbers[8] = alpha_dict['G']
    alpha_dict['E'] -= numbers[8]
    alpha_dict['I'] -= numbers[8]
    alpha_dict['G'] -= numbers[8]
    alpha_dict['H'] -= numbers[8]
    alpha_dict['T'] -= numbers[8]

    # eight
    numbers[1] = alpha_dict['O']
    alpha_dict['O'] -= numbers[1]
    alpha_dict['N'] -= numbers[1]
    alpha_dict['E'] -= numbers[1]

    # three
    numbers[3] = alpha_dict['R']
    alpha_dict['T'] -= numbers[3]
    alpha_dict['H'] -= numbers[3]
    alpha_dict['R'] -= numbers[3]
    alpha_dict['E'] -= numbers[3] * 2

    # seven
    numbers[7] = alpha_dict['S']
    alpha_dict['S'] -= numbers[7]
    alpha_dict['E'] -= numbers[7] * 2
    alpha_dict['V'] -= numbers[7]
    alpha_dict['N'] -= numbers[7]

    # nine
    numbers[9] = alpha_dict['E']
    alpha_dict['N'] -= numbers[9]
    alpha_dict['I'] -= numbers[9]
    alpha_dict['N'] -= numbers[9]
    alpha_dict['E'] -= numbers[9]

    answer = ""
    index = 0
    for num in numbers:
        answer += str(index) * num
        index += 1

    print "Case #{}: {}".format(question_id + 1, answer)
