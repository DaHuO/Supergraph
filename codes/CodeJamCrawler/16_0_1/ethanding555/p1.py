import numpy as np


def get_all_digit(num):
    result = []
    while (num > 0):
        result.append(num % 10)
        num = num / 10
    return result


def main():
    num_tests = int(input())
    tests = []
    result = []
    for i in range(1, num_tests + 1):
        tests.append(int(input()))
    
    for t in tests:
        checklist = np.zeros(10)
        n = 0
        while (not np.all(checklist) and n < 100000):
            n += 1
            cur = t * n
            digits = get_all_digit(cur)
            for digit in digits:
                checklist[digit] = 1
        if (n == 100000):
            result.append("INSOMNIA")
        else:
            result.append(cur)
        # print t, n

    for i in range(0, len(tests)):
        print "Case #{}: {}".format(i + 1, result[i])

if __name__ == "__main__":
    main()
