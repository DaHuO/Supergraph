__author__ = 'valeria'




def get_test():
    return int(raw_input())


def get_tests():
    tests_number = int(raw_input())
    tests = [get_test() for i in range(tests_number)]
    return tests


def get_number(n):
    s = set([i for i in range(10)])
    s_n = set()
    k = 2
    number = n
    while True:
        l = [int(i) for i in list(str(number))]
        for d in l:
            s_n.add(d)
        if s_n == s:
            return number
        number = n * k
        k += 1


def get_result(n):
    if n == 0:
        return "INSOMNIA"
    else:
        return get_number(n)

def main():
    tests = get_tests()
    for index, test in enumerate(tests):
        print("Case #{}: {}".format(index + 1, get_result(test)))

if __name__ == "__main__":
    main()