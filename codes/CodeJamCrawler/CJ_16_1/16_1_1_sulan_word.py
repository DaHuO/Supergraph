def print_result (case_num,result):
    print('Case #{}: {}'.format(case_num,result))

T = int(input())
for case_num in range(1,T+1):
    letters = input()
    word = letters[0]
    letters = letters[1:]
    for letter in letters:
        if letter < word[0]:
            word += letter
        else:
            word = letter + word
    print_result(case_num,word)

