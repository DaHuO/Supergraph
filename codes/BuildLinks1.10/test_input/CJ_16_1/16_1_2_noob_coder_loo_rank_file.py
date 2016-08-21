import collections


def get_missing_list(matrix):
    num_count = collections.defaultdict(int)

    for line in matrix:
        for digit in line:
            num_count[digit] += 1

    odd_nums = []
    for key, value in num_count.items():
        if value % 2 == 1:
            odd_nums.append(key)

    return sorted(odd_nums)


with open('B-large.in', 'r') as input, open('B-large.out', 'w') as output:
    num = int(input.readline())
    for case in range(num):
        N = int(input.readline())
        matrix = []
        for _ in range(2*N-1):
            line = map(int, input.readline().strip().split(' '))
            matrix.append(line)
        missing_list = get_missing_list(matrix)
        output_line = "Case #{num}: {missing_list}\n".format(
            num=case+1,
            missing_list=str(missing_list).replace('[', '').replace(']', '').replace(',', ' ')
        )
        output.write(output_line)
        # print output_line
