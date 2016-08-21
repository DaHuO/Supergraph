import sys

answer = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def check_answer(number, visited, multiplier):
    if number == '0':
        return 'INSOMNIA'

    number_str = str(int(number) * multiplier)

    for ch in number_str:
        visited[ch] = True
        if tuple(sorted(visited.keys())) == answer:
            return number_str

    return check_answer(number, visited, multiplier + 1)

with open(sys.argv[1]) as f:
    num_test_cases = int(f.readline().strip())

    count = 1
    for i in xrange(num_test_cases):
        line = f.readline().strip()
        last_number = check_answer(line, {}, 1)
        print('Case #{}: {}'.format(count, last_number))
        count += 1
