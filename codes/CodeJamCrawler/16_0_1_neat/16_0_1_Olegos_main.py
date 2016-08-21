input_file = open('in.txt', 'r')


def count_sheeps(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        s = set(str(n))
        n0 = n
        while s != set('0123456789'):
            n += n0
            s |= set(str(n))
        return n


numbers = []
for line in input_file:
    numbers.append(int(line))

output_file = open('out.txt', 'w')
case = 1
for n in numbers[1:]:
    output_file.write('Case #{}: {}\n'.format(case, count_sheeps(n)))
    case += 1
