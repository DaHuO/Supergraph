import sys


def strategy(number):
    mult = 1
    all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    s_number = str(number)
    digits_from_number = [int(s_number[i]) for i in range(len(s_number))]
    while set(digits_from_number) != set(all_digits):
        if number == 0:
            n_number = "INSOMNIA"
            break
        else:
            n_number = number * mult
            mult += 1
            s_number = str(n_number)
            for i in range(len(s_number)):
                digits_from_number.append(int(s_number[i]))
    return n_number

if __name__ == '__main__':
    f_n = sys.argv[1]
    f = open(f_n, 'r')
    c = f.readline()
    result = []
    for i in range(int(c)):
        n = f.readline()
        num = strategy(int(n))
        result.append(num)
    f.close()
    o_f = open("output %s" % f_n, 'w+')
    for i in range(len(result)):
        o_f.write("Case #%s: " % (i+1) + str(result[i]))
        o_f.write('\n')
    o_f.close()
