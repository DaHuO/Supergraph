# Google Code Jam 2016
# Qualification Round
# Problem 1 : Counting Sheep

def get_digits(n):
    digits = []
    n = str(n)
    for i in range(0, len(n)):
        digits.append(int(n[i]))
    return digits

if __name__ == "__main__":
    input_file = open('A-large.in', 'r')
    test_content = [int(x) for x in input_file.read().split('\n') if x != '']
    test_cases = test_content[1:]
    last_numbers = []

    for n in test_cases:
        numbers_seen = []
        last_seen = 0
        failure_hits = 0
        multiplier = 0
        while(len(numbers_seen) < 10):
            multiplier += 1
            new_number = n * multiplier
            if last_seen == new_number:
                failure_hits += 1
            else:
                last_seen = new_number
            numbers_seen = list(set(numbers_seen + get_digits(last_seen)))
            if failure_hits > 1000:
                last_seen = 'INSOMNIA'
                break
        last_numbers.append(last_seen)

    with open('output.txt', 'w') as f:
        case_number = 1
        for n in last_numbers:
            f.write('Case #{0}: {1}\n'.format(case_number, n))
            case_number += 1
