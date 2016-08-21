__author__ = 'ligenjian'


def form_num(num_list, k):
    result = 0
    for num in num_list:
        result = result * k + num
    return result


def solve(k, c):
    result = []
    min_count = (k - 1) / c + 1
    nums = range(k)
    for i in range(min_count):
        result.append(form_num(nums[i * c: (i + 1) * c], k))
    return min_count, map(lambda x: x + 1, result)

if __name__ == '__main__':
    input = open('input.txt', 'r')
    output = open('output.txt', 'w')
    t = int(input.readline())
    for i in range(t):
        k, c, s = map(int, input.readline().strip().split(' '))
        min_count, result = solve(k, c)
        if min_count > s:
            print>>output,  'Case #%d: IMPOSSIBLE' % (i + 1)
        else:
            print>>output, 'Case #%d: %s' % (i + 1, ' '.join(map(str, result)))
