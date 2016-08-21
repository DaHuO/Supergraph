import sys

__author__ = 'vandeen'

# Method for counting sheep for a non-zero int
def count_sheep(number):
    digits_seen = set()
    digits_possible = [d for d in range(10)]
    curr = number
    while True:
        digits = curr

        # Parse current number of digits and add them to the set
        while digits:
            digits_seen.add(digits % 10)
            digits //= 10

        if len(digits_seen.intersection(digits_possible)) is 10:
            return curr
        else:
            curr += number


if __name__ == "__main__":
    file = sys.argv[1]

    with open(file) as fh:
        fh.readline()  # Strip first line, don't need it
        case_num = 1
        output = open("test.out", "w")

        for n in fh:
            if int(n) is 0:
                print("Case #%d: INSOMNIA" % case_num)  # For debugging
                output.write("Case #%d: INSOMNIA\n" % case_num)
            else:  # run counting sheep method
                answer = count_sheep(int(n))
                print("Case #%d: %d" % (case_num, answer))  # For debugging
                output.write("Case #%d: %d\n" % (case_num, answer))
            case_num += 1