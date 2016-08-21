import sys


def count_sheep(num):
    digits = [False for x in range(10)]
    seen_so_far = set()
    index = 1
    while True:
        new_num = num * index
        temp = new_num
        while temp > 0:
            digits[temp % 10] = True
            temp /= 10

        if all(digits):
            return new_num

        if new_num in seen_so_far:
            return 'INSOMNIA'
        seen_so_far.add(new_num)
        index += 1


if __name__ == '__main__':
    num_test_cases = int(sys.stdin.readline().strip())
    for test_case in range(num_test_cases):
        num = int(sys.stdin.readline().strip())
        print "Case #%d: %s" % (test_case + 1, count_sheep(num))
