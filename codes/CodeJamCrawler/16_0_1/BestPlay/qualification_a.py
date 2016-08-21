import sys
import tempfile


def main():

    input_file_path = sys.argv[1]
    fd, output_file_path = tempfile.mkstemp(prefix='q_a_output.txt')
    print "output file: " + output_file_path
    with open(input_file_path) as inf, open(output_file_path, 'w') as outf:
        lines = inf.readlines()
        num_of_tests = int(lines[0].strip())

        print "num of tests: " + str(num_of_tests)

        for i in range(1, num_of_tests+1):
            N = int(lines[i].strip())
            last_num = calc_sleep(N)
            if last_num is None:
                outf.write("Case #{0}: INSOMNIA\n".format(i))
            else:
                outf.write("Case #{0}: {1}\n".format(i, last_num))


def calc_sleep(N):
    if N == 0:
        return None
    nums = set()
    i = 0
    while len(nums) != 10:
        i += 1
        nums.update(set(str(N*i)))

    return N*i


if __name__ == '__main__':
    main()
