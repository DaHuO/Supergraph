question_numbers = int(raw_input())

for result in xrange(0, question_numbers):
    job = list(raw_input())
    char_dict = {
        'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'N': 0, 'O': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Z': 0
    }
    for i in range(0, len(job)):
        for key in char_dict:
            if job[i] == key:
                char_dict[key] += 1
    # print char_dict
    numbers = [0]*10
    # 0
    numbers[0] = char_dict['Z']
    char_dict['Z'] -= numbers[0]
    char_dict['E'] -= numbers[0]
    char_dict['R'] -= numbers[0]
    char_dict['O'] -= numbers[0]
    # 2
    numbers[2] = char_dict['W']
    char_dict['T'] -= numbers[2]
    char_dict['W'] -= numbers[2]
    char_dict['O'] -= numbers[2]

    # 4
    numbers[4] = char_dict['U']
    char_dict['F'] -= numbers[4]
    char_dict['O'] -= numbers[4]
    char_dict['U'] -= numbers[4]
    char_dict['R'] -= numbers[4]

    # 6
    numbers[6] = char_dict['X']
    char_dict['S'] -= numbers[6]
    char_dict['I'] -= numbers[6]
    char_dict['X'] -= numbers[6]

    # 5
    numbers[5] = char_dict['F']
    char_dict['F'] -= numbers[5]
    char_dict['I'] -= numbers[5]
    char_dict['V'] -= numbers[5]
    char_dict['E'] -= numbers[5]

    # 8
    numbers[8] = char_dict['G']
    char_dict['E'] -= numbers[8]
    char_dict['I'] -= numbers[8]
    char_dict['G'] -= numbers[8]
    char_dict['H'] -= numbers[8]
    char_dict['T'] -= numbers[8]

    # 1
    numbers[1] = char_dict['O']
    char_dict['O'] -= numbers[1]
    char_dict['N'] -= numbers[1]
    char_dict['E'] -= numbers[1]

    # 3
    numbers[3] = char_dict['R']
    char_dict['T'] -= numbers[3]
    char_dict['H'] -= numbers[3]
    char_dict['R'] -= numbers[3]
    char_dict['E'] -= numbers[3] * 2
    
    # 7
    numbers[7] = char_dict['S']
    char_dict['S'] -= numbers[7]
    char_dict['E'] -= numbers[7] * 2
    char_dict['V'] -= numbers[7]
    char_dict['N'] -= numbers[7]

    # 9
    numbers[9] = char_dict['E']
    char_dict['N'] -= numbers[9]
    char_dict['I'] -= numbers[9]
    char_dict['N'] -= numbers[9]
    char_dict['E'] -= numbers[9]

    answer = ""
    index = 0
    for num in numbers:
        answer += str(index) * num
        index += 1

    print "Case #{}: {}".format(result + 1, answer)
