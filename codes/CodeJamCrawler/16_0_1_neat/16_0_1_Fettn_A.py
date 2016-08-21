import sys

def update(digits, current):
    while current:
        digits[current % 10] = True
        current //= 10

def run_test(case_number, generator):
    result = "INSOMNIA"
    base = int(next(generator))
    current = base
    digits = [False] * 10
    while base:
        update(digits, current)
        if all(digits):
            result = str(current)
            break
        current += base

    print('Case #%d: %s' % (case_number, result))

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