__author__ = 'valeria'
def get_test():
    a = list(raw_input())
    return a


def get_tests():
    tests_number = int(raw_input())
    tests = [get_test() for i in range(tests_number)]
    return tests


def get_result(l):
    cur = l[0]
    if l[len(l) - 1] == '-':
        n = 1
    else:
        n = 0
    for c in l[1:]:
        if c != cur:
            n += 1
            cur = c
    return n

def main():
    tests = get_tests()
    for index, test in enumerate(tests):
        print("Case #{}: {}".format(index + 1, get_result(test)))

if __name__ == "__main__":
    main()
