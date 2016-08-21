import math

def multiset(string):
    char_set = set(string)
    char_dict = {}
    for char in char_set:
        char_dict[char] = string.count(char)
    return char_dict

def substract(mset1, mset2, c=1):
    for char in mset1:
        mset2[char] -= mset1[char]*c
    return mset2

def calculate_count(num, char, string, total_char_dict):
    count = total_char_dict.get(char, 0)
    if count != 0:
        substract(char_dicts[num], total_char_dict, count)
    return count

def solve(string):
    total_char_dict = multiset(string)

    counts = [0] * 10
    counts[0] = calculate_count(0, 'Z', string, total_char_dict)
    counts[2] = calculate_count(2, 'W', string, total_char_dict)
    counts[4] = calculate_count(4, 'U', string, total_char_dict)
    counts[6] = calculate_count(6, 'X', string, total_char_dict)
    counts[8] = calculate_count(8, 'G', string, total_char_dict)
    counts[3] = calculate_count(3, 'H', string, total_char_dict)
    counts[5] = calculate_count(5, 'F', string, total_char_dict)
    counts[7] = calculate_count(7, 'V', string, total_char_dict)
    counts[9] = calculate_count(9, 'I', string, total_char_dict)
    counts[1] = calculate_count(1, 'O', string, total_char_dict)

    ans = ''
    for i in range(10):
        ans += str(i) * counts[i]
    return ans

fname = 'test.txt'
fname = 'A-small-attempt1.in'
fname = 'A-large.in'
fin = open(fname)
lines = fin.readlines()
fin.close()

strings = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
char_dicts = [multiset(strings[i]) for i in range(10)]

for k, line in enumerate(lines[1:]):
    string = line.strip()
    ans = solve(string)
    print('Case #%d: %s' % (k+1, ans))

    recover = ''
    for i in ans:
        recover += strings[int(i)]
    if sorted(string) != sorted(recover):
        print(string)
        print(recover)
        print('False')
