def main():
    file = open('in.txt', 'r')
    data = file.read()
    file.close()

    lines = data.split("\n")
    n = int(lines[0])
    result = ''
    for i in range(1, n + 1):
        num = int(lines[i])
        ret = solve(num)
        result += 'Case #' + str(i) + ': ' + ret + "\n"

    file = open('out.txt', 'w')
    file.write(result)
    file.close()


def solve(n):
    if (n == 0):
        return 'INSOMNIA'
    arr = [False] * 10
    merge_digits(n, arr)
    digits = count_digits(n) + 1
    max = 10 ** digits
    for i in range(2, max + 1):
        a = n * i
        merge_digits(a, arr)
        if (check_digits(arr) == True):
            return str(a)
    return 'INSOMNIA'

def merge_digits(n, arr):
    a = n
    while (a != 0):
        b = int(a % 10)
        a = int(a / 10)
        arr[b] = True

def check_digits(arr):
    for i in range(len(arr)):
        if (arr[i] == False):
            return False
    return True

def count_digits(n):
    a = n
    count = 0
    while (a != 0):
        a = int(a / 10)
        count += 1
    return count


main()