__author__ = 'Parth'


def all_digits(digits):
    for i in range(10):
        if not digits[i]:
            return False
    return True


def get_digits(number, digits):
    num_str = str(number)
    for i in num_str:
        digits[int(i)] = True


if __name__ == "__main__":
    T = input()
    T = int(T)
    inputs = []

    for i in range(T):
        a = input()
        inputs.append(int(a))

    case = 0

    for N in inputs:
        case += 1
        if N == 0:
            result = "INSOMNIA"
        else:
            digits = [False for i in range(10)]
            i = 1
            while not all_digits(digits):
                get_digits(N * i, digits)
                i += 1
            result = str(N*(i-1))
        print("Case #%d: %s" % (case, result))
