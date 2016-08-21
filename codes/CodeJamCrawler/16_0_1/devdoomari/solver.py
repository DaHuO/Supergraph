import sys

input_lines = sys.stdin.read().split('\n')
# input_lines = open('./A-small-practice.in', 'r').read().split('\n')
# input_lines = open('./test_input.txt', 'r').read().split('\n')
case_count = int(input_lines[0])

def is_solved(digits_hit):
    for i in range(len(digits_hit)):
        if not digits_hit[i]:
            return False
    return True

def hit_digits(number, digits_hit):
    # print("got: " + str(number))
    # import pudb;pudb.set_trace()
    digit_str_list = list(str(number))
    for digit_str in digit_str_list:
        digit_int = int(digit_str)
        digits_hit[digit_int] = True

def solve(original):
    digits_hit = [
        False, #0
        False, #1
        False, #2
        False, #3
        False, #4
        False, #5
        False, #6
        False, #7
        False, #8
        False, #9
    ]
    if original == 0:
        return "INSOMNIA"
    n = 1
    while not is_solved(digits_hit):
        hit_digits(n * original, digits_hit)
        n = n + 1
    return (n - 1) * original

for i in range(1, len(input_lines)):
    input_line = input_lines[i]
    if len(input_line) == 0:
        continue
    n = int(input_line)
    # print(n)
    print("Case #{i}: {result}".format(
        i=i, result=solve(n)
    ))
    # print(type(max_shy))
