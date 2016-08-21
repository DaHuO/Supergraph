__author__ = 'fdoherty'

def output(case, data):
    print 'Case #%s:' % case, data

def letter_counts(S):
    result = dict()
    for l in S:
        if l not in result:
            result[l] = 0
        result[l] += 1
    return result

def process_word(d, letters):
    count = 0
    new_letters = letters.copy()
    while True:
        for z in d:
            if z not in new_letters:
                return count, letters
            else:
                new_letters[z] -= 1
                if new_letters[z] <= 0:
                    new_letters.pop(z)
        letters = new_letters.copy()
        count += 1

DIGITS = {'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9'}

def solve(case_num, S):
    result = dict()
    letters = letter_counts(S)
    for x in ('ZERO', 'TWO', 'SIX', 'EIGHT', 'SEVEN', 'FIVE', 'NINE', 'FOUR', 'THREE', 'ONE'):
        count, letters = process_word(x, letters)
        result[DIGITS[x]] = count
    if len(letters.keys()) > 0:
        print 'ERROR'
    result_str = ''
    for x in range(10):
        if str(x) in result:
            result_str += str(x) * result[str(x)]
    output(case_num, result_str)

NUM_CASES = input()
for test_num in range(NUM_CASES):
    S = raw_input()
    solve(test_num+1, S)