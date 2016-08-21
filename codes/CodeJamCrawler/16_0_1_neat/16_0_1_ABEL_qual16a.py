from collections import defaultdict


def count_digits(num):
    digit_count = defaultdict(int)
    for character in num:
        digit_count[character] += 1
    return digit_count


def count_iterations(start_num):
    if 2 * start_num == start_num:
        return 'INSOMNIA'

    current_mult = 1
    overall_counts = {str(key): 0 for key in range(10)}
    while min(overall_counts.values()) < 1:
        new_counts = count_digits(str(current_mult * start_num))
        for key in new_counts:
            overall_counts[key] += 1
        current_mult += 1

    return (current_mult - 1) * start_num


def handle_file(infile):
    num_cases = int(infile.readline())
    cases = infile.readlines()
    answers = []

    for i in range(num_cases):
        answers.append(count_iterations(int(cases[i])))

    for i in range(num_cases):
        print('Case #{0}: {1}'.format(i + 1, answers[i]))


if __name__ == '__main__':
    with open("A-large.in", "r") as f:
        handle_file(f)
