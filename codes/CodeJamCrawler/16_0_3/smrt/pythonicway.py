import math
from random import choice
# answers = []

tried_numbers = []
acceptable_numbers = {}

def is_not_prime(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return False

def base_maker(n):
    divisors = []
    for i in range(2, 11):
        to_test = int(n, i)
        ans = is_not_prime(to_test)
        if ans:
            divisors.append(ans)
        else:
            return False
    return divisors

def jam(n, j):
    while len(acceptable_numbers) < j:
        test = "1"
        for i in range(n-2):
            test += choice("01")
        test += "1"
        if test not in tried_numbers:
            tried_numbers.append(test)
            divisors = base_maker(test)
            if divisors:
                acceptable_numbers[test] = divisors
"""
with open("small") as f:
    lines = f.readlines()[1:]
    for i, string in enumerate(lines, 1):
        answers.append("Case #{}: {}".format(i, jam(string.rstrip())))
"""
jam(16, 50)

with open("answers.txt", "w") as f:
    answers = ["Case #1:"]
    for number in acceptable_numbers:
        string = str(number)
        for div in acceptable_numbers[number]:
            string += " " + str(div)
        answers.append(string)
    f.write("\n".join(answers))

"""
with open("answers.txt", "w") as f:
    f.write("\n".join(answers))
"""
