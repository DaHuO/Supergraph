# Tejas Deshpande
# GCJ 2016 Round 1A
# Problem A
# 04/15/2016

from collections import deque

def get_winning_string(contest_string):
    contest_string = list(contest_string)
    contest_string.reverse()
    first_word = deque(contest_string.pop())
    for num_words in range(len(contest_string)):
        curr_letter = contest_string.pop()
        if curr_letter >= first_word[0]:
            first_word.appendleft(curr_letter)
        else:
            first_word.append(curr_letter)

    return ''.join(first_word)



if __name__ == "__main__":
    num_test_cases = input()
    num_test_cases = int(num_test_cases)

    for test_case in range(num_test_cases):
        contest_string = input()
        print('Case #' + str(test_case+1) + ': ' + get_winning_string(contest_string))
