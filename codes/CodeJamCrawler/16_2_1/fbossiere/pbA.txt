temp_res = []
with open("C:/Users/paco/Dropbox/algorithms/google_jam/A-large.in") as input_file:
    for i, line in enumerate(input_file):
        if i==0:
            n = int(line)
        else:
            temp_res.append(line.replace('\n', ''))

cases = temp_res
from collections import Counter, OrderedDict

def solve(case):
    digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    sentence = Counter(case)
    res = []
    char_dict = [('W', 2), ('G', 8), ('Z',0), ('X',6), ('U',4), ('H',3), ('F',5), ('I',9), ('V',7), ('O',1)]
    for char, corresponding_number in char_dict:
        while char in sentence:
            for letter in digits[corresponding_number]:
                sentence[letter] -= 1
                if sentence[letter] == 0:
                    del sentence[letter]
            res.append(corresponding_number)
    return ''.join([str(val) for val in sorted(res)])



output_path = "C:/Users/paco/Dropbox/algorithms/google_jam/A-large.out"
with open(output_path, mode='w') as output:
    for case in cases:
        answer = solve(case)
        output.write("Case #{i}: ".format(i=case[0]) + str(answer) + '\n')