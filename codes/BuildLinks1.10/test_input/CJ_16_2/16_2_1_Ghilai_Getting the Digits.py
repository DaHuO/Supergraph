
FILE_PATH = "A-small-attempt0.in"
OUTPUT_FILE_PATH = 'A-small-attempt0.out'

LETTERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
NOT_FOUND_DIGIT = "NOT_FOUND"

def read_file(path):
    with open(path, 'rb') as f:
        lines = f.readlines()
        test_cases = [line for line in lines[1:]]
        for (i, test_case) in enumerate(test_cases):
            if test_case.endswith('\n'):
                test_cases[i] = test_case[:-1]
    print test_cases
    return test_cases

def output_solution(solution, path):
    lines = []
    with open(path, 'wb') as f:
        for (i, sol) in enumerate(solution):
            lines += ['Case #{index}: {solution}\n'.format(index=i+1, solution=sol)]
        f.writelines(lines)
    
def get_str_without_letter(S, digit):
    original = S
    for letter in digit:
        if letter not in S:
            # the string doesn't contain the digit
            return NOT_FOUND_DIGIT
        # remove the letter from S
        index = S.index(letter)
        S = S[:index] + S[index + 1:]
    # removed the entire digit from S! good.
    return S
     
            
    
def solve_test_case(S):
    letter_index = 0
    digits_found = []
    while S:
        current_number = LETTERS[letter_index]
        new_S = get_str_without_letter(S, current_number)
        if new_S == NOT_FOUND_DIGIT:
            # digit not in S
            letter_index += 1
            while letter_index >= len(LETTERS):
                # found bad numbers. populate last number.
                bad_digit = digits_found[-1]
                # append its letters back to S (we removed it earlier)
                S = bad_digit + S
                # continue trying without this number
                letter_index = LETTERS.index(bad_digit) + 1
                # remove it from the digits found so far
                digits_found = digits_found[:-1]
                
        else:
            # define S to be S minus current_number
            S = new_S
            digits_found.append(current_number)
    
    return "".join([str(LETTERS.index(l)) for l in digits_found])
                
    
if __name__ == "__main__":
    test_cases = read_file(FILE_PATH)
    solution = [solve_test_case(test_case) for test_case in test_cases]
    print solution
    output_solution(solution, OUTPUT_FILE_PATH)