__author__ = 'valeria'


def get_test():
    a = [int(i) for i in raw_input().split()]
    return a


def get_tests():
    tests_number = int(raw_input())
    tests = [get_test() for i in range(tests_number)]
    return tests


def get_result(l):
    k = l[0]
    c = l[1]
    s = l[2]
    l = " ".join([str(1 + i * k ** (c - 1)) for i in range(k)])
    return l

def main():
    tests = get_tests()
    for index, test in enumerate(tests):
        print("Case #{}: {}".format(index + 1, get_result(test)))

if __name__ == "__main__":
    main()
