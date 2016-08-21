import sys


def count_switches(stack):
    zone_changes = stack.count('+-') + stack.count('-+')
    if stack[-1] == '-':
        return zone_changes + 1
    return zone_changes


def main():
    task_input = open(sys.argv[1], 'r')
    task_output = open(sys.argv[1] + '.out', 'w')
    cases_count = int(task_input.readline())
    for case in range(1, cases_count + 1):
        switches = count_switches(task_input.readline().rstrip())
        task_output.write('Case #{}: {}\n'.format(case, switches))
    task_input.close()
    task_output.close()


main()
