import math

def main():
    file = open('in.txt', 'r')
    data = file.read()
    file.close()

    lines = data.split("\n")
    n = int(lines[0])
    result = ''
    for i in range(1, n + 1):
        s = lines[i]
        nj = s.split(' ')
        n = int(nj[0])
        j = int(nj[1])
        ret = solve(n, j)
        result += 'Case #' + str(i) + ': \n' + ret

    file = open('out.txt', 'w')
    file.write(result)
    file.close()


def solve(n, j):
    max = 2 ** (n - 2)
    count = 0
    ret = ''
    for i in range(max + 1):
        # double to get last '0'
        v = i * 2
        # convert to binary string
        bin = dec_to_bin(v)

        found = True
        arr = [-1] * 9
        for b in range(2, 11):
            # convert to decimal value from base b
            dec = string_to_dec(bin, b)
            # get value of 1xxx1
            sum = b ** (n - 1) + 1
            # add dec to sum to get final value
            value = sum + dec
            # check whether value is prime
            division = is_prime(value)
            arr[b - 2] = division
            if division == -1:
                found = False
                break
        if found == False:
            continue

        # if we found it
        # get decimal representation of the number
        sum = 10 ** (n - 1) + 1
        sum += int(bin)
        ret += str(sum) + ' ' + ' '.join(str(x) for x in arr) + '\n'
        count += 1
        if count == j:
            break

    return ret

def dec_to_bin(n):
    return "{0:b}".format(n)

# string of 0 and 1 to dec given any base
def string_to_dec(str, base):
    if base == 10:
        return int(str)
    p = len(str) - 1
    n = 0
    for i in range(len(str)):
        if str[i] == '1':
            n += base ** (p - i)
    return n

def is_prime(n):
    if n in [0, 1, 2, 3, 5, 7]:
        return -1
    if n % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return -1

main()