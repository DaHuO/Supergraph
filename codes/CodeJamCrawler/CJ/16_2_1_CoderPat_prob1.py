from collections import defaultdict

num_cases = int(input())
for i in range(num_cases):

    input_str = input()

    letter_count = defaultdict(lambda:0)
    for letter in input_str:
        letter_count[letter] += 1

    number_count = [0]*10

    number_count[0] = letter_count['Z']
    letter_count['Z'] -= number_count[0]
    letter_count['E'] -= number_count[0]
    letter_count['R'] -= number_count[0]
    letter_count['O'] -= number_count[0]

    number_count[2] = letter_count['W'] 
    letter_count['T'] -= number_count[2]
    letter_count['W'] -= number_count[2]
    letter_count['O'] -= number_count[2]

    number_count[4] = letter_count['U']
    letter_count['F'] -= number_count[4]
    letter_count['O'] -= number_count[4]
    letter_count['U'] -= number_count[4]
    letter_count['R'] -= number_count[4]

    number_count[5] = letter_count['F']
    letter_count['F'] -= number_count[5]
    letter_count['I'] -= number_count[5]
    letter_count['V'] -= number_count[5]
    letter_count['E'] -= number_count[5]

    number_count[7] = letter_count['V']
    letter_count['S'] -= number_count[7]
    letter_count['E'] -= number_count[7]
    letter_count['V'] -= number_count[7]
    letter_count['E'] -= number_count[7]
    letter_count['N'] -= number_count[7]

    number_count[6] = letter_count['X'] 
    letter_count['S'] -= number_count[6]
    letter_count['I'] -= number_count[6]
    letter_count['X'] -= number_count[6]

    number_count[1] = letter_count['O'] 
    letter_count['O'] -= number_count[1]
    letter_count['N'] -= number_count[1]
    letter_count['E'] -= number_count[1]

    number_count[9] = int(letter_count['N']/2)
    letter_count['N'] -= number_count[9]
    letter_count['I'] -= number_count[9]
    letter_count['N'] -= number_count[9]
    letter_count['E'] -= number_count[9]

    number_count[8] = letter_count['I']
    letter_count['E'] -= number_count[8]
    letter_count['I'] -= number_count[8]
    letter_count['G'] -= number_count[8]
    letter_count['H'] -= number_count[8]
    letter_count['T'] -= number_count[8]

    number_count[3] = letter_count['T']
    letter_count['T'] -= number_count[3]
    letter_count['H'] -= number_count[3]
    letter_count['R'] -= number_count[3]
    letter_count['E'] -= number_count[3]
    letter_count['E'] -= number_count[3]

    string_num = ""
    for j, num in enumerate(number_count):
        string_num += num*str(j)

    print("Case #%s: %s" % (i+1, string_num))














