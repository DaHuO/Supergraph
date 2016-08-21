import sys

def sheep(n):
    if n == 0:
        return "INSOMNIA"

    digits = set(range(0, 10))
    current_number = n
    while digits:
        string_version_of_current_number = str(current_number)
        digits_to_remove = map(int, list(string_version_of_current_number))
        digits = digits.difference(digits_to_remove)
        if not digits:
            break
        current_number += n

    return current_number



if __name__ == "__main__":
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = int(raw_input())  # read a list of integers
        print "Case #{}: {}".format(i, sheep(n))
