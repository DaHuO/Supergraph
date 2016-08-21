import sys


def main():
    inputs = next(sys.stdin)
    nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    case_num = 0
    for line in sys.stdin:
        case_num += 1
        num = int(line)
        nums_seen = []

        for ch in str(num):
            nums_seen.append(int(ch))

        if num == 0:
            print "Case #{}: INSOMNIA".format(case_num)
            continue

        iter = 1
        while True:
            new_num = iter * num;
            iter += 1

            for ch in str(new_num):
                nums_seen.append(int(ch))

            if set(nums_seen) >= nums:
                print "Case #{}: {}".format(case_num, new_num)
                break


if __name__ == '__main__':
        exit(main())
