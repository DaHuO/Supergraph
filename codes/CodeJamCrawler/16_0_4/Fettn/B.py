import sys

def calculate_position(p, k, c):
    result = 0
    for i in range(c):
        result += p * (k ** i)
    return result

def run_test(case_number, generator):
    k, c, s = (int(x) for x in next(generator).split())
    result = [str(calculate_position(x, k, c) + 1) for x in range(k)]
    print('Case #%d: %s' % (case_number, ' '.join(result)))

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()