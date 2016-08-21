if __name__ == '__main__':
    inp = open("large_input.txt", "r")
    out = open("large_output.txt","w")
    test_cases = [x.strip('\n') for x in inp.readlines()]
    test_case_num = 1
    while test_case_num <= int(test_cases[0]):
        test_case = test_cases[test_case_num]
        winning_word = test_case[0]
        for char in test_case[1:]:
            if char >= winning_word[0] :
                winning_word = char + winning_word
            else :
                winning_word += char
        out.write('Case #{}: {}\n'.format(test_case_num,winning_word))
        test_case_num += 1

