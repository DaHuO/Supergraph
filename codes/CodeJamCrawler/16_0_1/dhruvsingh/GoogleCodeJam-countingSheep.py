final_list = []


def check_number(num, num_split):
    num_set = set()
    num_set.update(num_split)
    cnt = 2

    while len(num_set) != 10:
        calc = num * cnt
        cnt += 1
        num_split = map(int, str(calc))
        num_set.update(num_split)
    else:
        return calc


def process_test_cases(T):
    for _ in xrange(T):
        num_split = map(int, raw_input())
        num = int(''.join(map(str, num_split)))

        if num == 0:
            final_list.append('INSOMNIA')
            continue
        else:
            number = check_number(num, num_split)
            final_list.append(number)

T = input()
process_test_cases(T)

for index, num in enumerate(final_list):
    print 'Case #{}: {}'.format(index + 1, num)
