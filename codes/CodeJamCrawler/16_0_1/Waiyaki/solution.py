def count_to_sleep(number):
    numbers = set()
    target = set(range(10))
    index = 2

    for n in str(number):
        numbers.add(int(n))
    if number == 0:
        return 'INSOMNIA'
    elif numbers == target:
        return number
    while True:
        num = number * index
        for n in str(num):
            numbers.add(int(n))
        if numbers == target:
            return num
        index += 1


def readfile(file):
    with open(file, 'r') as fin:
        testcases = fin.readline()
        numbers = [int(i.strip()) for i in fin.readlines()]
    return numbers, testcases


def main():
    numbers, testcases = readfile('A-large.in')
    with open('large-output.in', 'w') as outfile:
        for index, num in enumerate(numbers):
            ans = str(count_to_sleep(num))
            outfile.write('Case #' + str(index + 1) + ': ' + ans + '\n')

if __name__ == '__main__':
    main()
