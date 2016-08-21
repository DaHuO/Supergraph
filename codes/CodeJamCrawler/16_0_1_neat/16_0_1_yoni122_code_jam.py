
def containing_digits(number):
    res = []
    while number > 0:
        res.append(number % 10)
        number = number / 10

    return res


def find_last_number(number):

    key_hash = {}
    i = 0
    if number == 0:
        return "INSOMNIA"
    while len(key_hash) < 10:
        i += 1
        digit_list = containing_digits(number * i)
        for digit in digit_list:
            key_hash[digit] = 'Y'

    return number * i





def main(input_file, output_file):

    with open(input_file) as input:
        number_list = input.readlines()

    print "Got {0} input numbers".format(number_list[0])


    number_list.pop(0)

    with open (output_file, 'w') as output:
        for idx, val  in enumerate(number_list):
            val = int(val)
            last_number = find_last_number(val)
            print "Last number for {0} is : {1}".format(val, last_number)

            output.write("Case #{0}: {1}\n".format(idx + 1, last_number))
    return


if __name__ == "__main__":
    input_file = "A-large.in"
    output_file = "A-large.out"
    main(input_file, output_file)