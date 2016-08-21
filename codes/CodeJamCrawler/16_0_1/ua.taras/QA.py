import sys


def when_asleep(n, k, digits_set):
    if n == 0:
        return 'INSOMNIA'
    kn = k * n
    digits = list(str(kn))
    for digit in digits:
        digits_set.add(digit)
    if len(digits_set) == 10:
        return str(kn)
    return when_asleep(n, k+1, digits_set)


def main():
    task_input = open(sys.argv[1], 'r')
    task_output = open(sys.argv[1] + '.out', 'w')
    cases_count = int(task_input.readline())
    for case in range(1, cases_count + 1):
        asleep = when_asleep(int(task_input.readline()), 1, set())
        task_output.write('Case #{}: {}\n'.format(case, asleep))
    task_input.close()
    task_output.close()


main()
