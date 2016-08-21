def is_jamcoin(length, num_jamcoins):

    jamcoins = 0
    for a in range(2 ** (length - 2)):
        if jamcoins < num_jamcoins:
            binary_num = int("{0:b}".format(a))
            test = (str("1{0:0=14d}1".format(binary_num)))
            divisors = []
            for base in range(2, 11):
                num = int(test, base)
                numm = first_divisor(num)
                if numm is not None:
                    divisors.append(str(numm))
                else:
                    break
                if len(divisors) == 9:
                    string = "{} {}".format(test, ' '.join(divisors))
                    strings.append(string)
                    jamcoins += 1
                    print(jamcoins)
        else:
            break


def first_divisor(num):
    import math
    for i in range(2, math.ceil(num ** 0.5) + 1):
        if num % i == 0:
            return i
    return None


strings = []

with open("input.txt", 'r') as input_file:
    cases = input_file.readline()
    data = input_file.readline()
    data = data.split(' ')
    n = int(data[0])
    j = int(data[1])
    is_jamcoin(n, j)
with open("output.txt", 'w') as output_file:
    output_file.write("Case #1:\n")
    for string in strings:
        if string is not strings[-1]:
            output_file.write("{}\n".format(string))
        else:
            output_file.write("{}".format(string))


