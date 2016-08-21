def count_on_base(n, base):
    result_number = 0
    for power, multiplier in enumerate(n[::-1]):
        result_number += (base ** power) * multiplier
    return result_number


def check_is_prime(number):
    for submultiple in range(2, int((number + 1) ** 0.5)):
        if number % submultiple == 0:
            return submultiple
    return 0


class Answer:
    def __init__(self, answer, multiples_list):
        self.answer = answer + answer
        self.multiples_list = multiples_list

    def __str__(self):
        return " ".join(map(str, [self.answer] + self.multiples_list))


def run(test):
    answers = []
    n, j = test.split(" ")
    n, j = int(n), int(j)
    number = [0] * n
    number[0] = 1
    number[n-1] = 1
    for possible_number in range(2 ** 14):
        if len(answers) >= j:
            break
        possible_number = map(int, list(bin(possible_number)[2:]))
        number[1:-1] = [0] * (n - 2 - len(possible_number)) + possible_number
        possible_multipliers = []
        for base in range(2, 11):
            multiplier = check_is_prime(count_on_base(number, base))
            if multiplier:
                possible_multipliers.append(multiplier)
            else:
                break
        if len(possible_multipliers) == 9:
            answers.append(Answer("".join(map(str, number)), possible_multipliers))
    return "\n".join(map(str, answers))


t = int(raw_input("").rstrip())
for i in range(t):
    print "Case #%s:\n%s" % (i + 1, run(raw_input("").rstrip()))
