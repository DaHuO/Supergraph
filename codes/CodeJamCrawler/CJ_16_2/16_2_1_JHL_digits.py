import sys

filename = sys.argv[1]
fo = open(filename, 'r')
input_raw = fo.read()
fo.close()
input_lines = input_raw.split("\n")
num_cases = int(input_lines[0])

def numbers(strnum):
    IDENTIFIERS = [('ZERO', 'Z'), ('SIX', 'X'), ('SEVEN', 'S'), ('FIVE', 'V'), ('FOUR', 'F'), ('THREE', 'R'), ('EIGHT', 'G'), ('TWO', 'W'), ('ONE', 'O'), ('NINE', 'E')]
    DIGITS = {'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8, 'NINE':9}
    counts = [0] * 10
    char_counts = {}
    for c in strnum:
        if char_counts.has_key(c):
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    for num, iden in IDENTIFIERS:
        iden_counts = {}
        for c in num:
            if iden_counts.has_key(c):
                iden_counts[c] += 1
            else:
                iden_counts[c] = 1
        if char_counts.has_key(iden) and char_counts[iden] > 0:
            count = char_counts[iden]
            for char, char_count in iden_counts.items():
                char_counts[char] -= count * char_count
            counts[DIGITS[num]] = count
        else:
            counts[DIGITS[num]] = 0
    return counts

def phone_number(counts):
    number = ''
    for i in range(len(counts)):
        for j in range(counts[i]):
            number += str(i)
    return number

numbers_lst = []
for i in range(num_cases):
    numbers_lst.append(phone_number(numbers(input_lines[i + 1])))

fo = open('out.txt', 'w')
for i in range(num_cases):
    fo.write('Case #' + str(i + 1) + ': ' + numbers_lst[i])
    if i != num_cases - 1:
        fo.write("\n")
fo.close()
