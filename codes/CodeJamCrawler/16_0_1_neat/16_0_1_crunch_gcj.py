import argparse


def solve(i, number):
    if number == 0:
        answer = 'INSOMNIA'
    else:
        nums = set([])
        j = 1
        while len(nums) < 10:
            nums = nums.union(set(str(number * j)))
            j += 1
        answer = number * (j - 1)
    print 'Case #{}: {}'.format(i, answer)


def main(input_file):
    with file(input_file, 'r') as f:
        test_cases = int(f.readline())
        for i in xrange(test_cases):
            solve(i + 1, int(f.readline()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Google Code Jam solution.')
    parser.add_argument('input_file', help='Input file.')

    args = parser.parse_args()
    main(args.input_file)
