'''
CodeJam 2016:
    Problem A. Counting Sheep
'''


def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'
    seen_numbers = set([])
    i = 1
    while True:
        count = i * n
        numbers = list(str(count))
        seen_numbers = seen_numbers.union(set(numbers))
        if seen_numbers == set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            return count
        else:
            i += 1
        if i >= 1000:
            return 'INSOMNIA'

with open('A-large.in') as input_file:
    cases = map(lambda x: int(x[:-1]), input_file.readlines()[1:])
output = []

for i, case in enumerate(cases, start=1):
    res = count_sheep(case)
    output.append('Case #{}: {}\n'.format(i, res))

with open('a-output.txt', mode='r+') as f:
    f.writelines(output)
