import random

"""
1. Each digit is mapped to False.
2. Multiples
3. If the digit is spotted, mark true.
"""
def test_num(n):

    if (n == 0):
        return "INSOMNIA"

    num_sheep = 0
    nums_spotted = [False] * 10
    
    while (num_sheep < 500 and all(nums_spotted) == False):
        num_sheep += 1
        my_num = num_sheep * n
        my_digits = num_to_digit_list(my_num)
        for digit in my_digits:
            nums_spotted[digit] = True
            
    if (all(nums_spotted) == False):
        return "INSOMNIA"
    else:
        return my_num

"""
Repeatedly divides by ten and appends the remainder.

Will be backwards, but that doesn't matter in this problem
"""
def num_to_digit_list(n):
    digit_list = []
    while (n >= 1):
        quotient = n / 10
        remainder = n - (quotient * 10)
        digit_list.append(remainder)
        n = quotient
    return digit_list
        
#for n in range(100):
#    my_num = random.randrange(1000000)
#    print my_num, test_num(my_num)

def run(file_name):
    f = open("A-large.in", "r")
    g = open("A-large.out", "w")
    num_test_cases = int(f.readline())
    for case_no in range(1, num_test_cases + 1):
        line = int(f.readline())
        message = "Case #" + str(case_no) + ": " + str(test_num(line))
        print message
        g.write(message + "\n")

run(None)
