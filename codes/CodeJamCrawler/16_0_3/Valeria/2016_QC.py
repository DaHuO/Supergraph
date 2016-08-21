__author__ = 'valeria'

import itertools

def get_test():
    l = [int(i) for i in raw_input().split()]
    return (l[0], l[1])


def get_tests():
    tests_number = int(raw_input())
    tests = [get_test() for i in range(tests_number)]
    return tests

def check_result(s):
    for i in range(2, 11):
        if int(s, i) % (i+1) != 0:
            return False
    return True

def get_result(test):
    n = test[0]
    j = test[1]
    results = []
    for s in itertools.product([0,1], repeat=n-2):
        s = "".join([str(k) for k in list(s)])
        result = []
        s = "1" + s + "1"
        if int(s, 10) % 11 == 0:
            result.append(s)
            result += range(3, 12)
            if check_result(s):
                results.append(result)
        if len(results) == j:
            return results
    print "aaa"
    return results


def main():
    tests = get_tests()
    for index, test in enumerate(tests):
        print("Case #{}: ".format(index + 1))
        result = get_result(test)
        for r in result:
            for d in r:
                print d,
            print
        print

if __name__ == "__main__":
    main()