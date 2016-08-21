import math
def count_occurence(digit_str_list, digit_word):
    digit_word_count = {}
    for d in digit_word:
        digit_word_count[d] = 0
    for s in digit_str_list:
        if s in digit_word:
            digit_word_count[s] = digit_word_count[s] + 1
    if digit_word_count:
        min_count = 2000
        for k, v in digit_word_count.iteritems():
            min_count = min(min_count, v)
    else:
        min_count = 0
        return digit_str_list, 0

    word_to_remove = []
    for i in range(0, min_count):
        for d in digit_word:
            word_to_remove.append(d)
    for w in word_to_remove:
        digit_str_list.remove(w)
    return digit_str_list, min_count


def Digit(digit_str):
    digit_str_list = list(digit_str)
    digits_to_check = [0,2,4,8,6,7,5,9,3,1]
    digit_words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    final_digits = {}
    final_digit_str = ''
    #digits = range(0, 10)
    for i in digits_to_check:
        digit_str_list, occurence = count_occurence(digit_str_list, digit_words[i])
        final_digits[i] = occurence
    for i in range(0, 10):
        if i in final_digits:
            for _ in range(0, final_digits[i]):
                final_digit_str += str(i)
    return final_digit_str


def Digit_in():
    test_case_num = int(raw_input())
    for test_case in range(1, test_case_num+1):
        print 'Case #%s: %s' % (test_case, Digit(raw_input()))

Digit_in()