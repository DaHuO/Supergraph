def digit_set(num):
    found = set()
    while num > 0:
        found.add(num % 10)
        num //= 10
    return found

def check_for_digits(num):
    if num == 0: return -1

    current_num = -num
    digits = set([0,1,2,3,4,5,6,7,8,9])
    while digits:
        current_num += num
        digits -= digit_set(current_num)
    return current_num

def check_all():
    for num in range(1000000):
        result = check_for_digits(num)
        if result == -1:
            print(num)

def process_input(fileobj):
    """Given an already open file object, reads the data."""
    testcases = int(fileobj.readline().strip())
    for testcase in range(testcases):
        num = int(fileobj.readline().strip())
        result = check_for_digits(num)
        if result == -1: result = "INSOMNIA"
        print("Case #{}: {}".format(testcase+1,result))

import fileinput
def driver():
    f = fileinput.input(files=('sheep-large-in.txt'))
    process_input(f)

if __name__ == "__main__":
    driver()


