__author__ = 'avital'


def sheep_count(chosen_number):

    all_digits = []

    for num in range(0, 10):
        all_digits.append(str(num))

    digits = []
    i = 1

    while True:

        if chosen_number == 0:
            return 'INSOMNIA'

        for digit in str(chosen_number*i):

            if digit not in digits:
                digits.append(digit)
                digits.sort()

            if digits == all_digits:
                return chosen_number*i

        i += 1


def main():

    input_file = open('sheep_large.in', 'r')
    input = input_file.readlines()

    output = open('sheep_large_result.txt', 'w')
    cases = input.pop(0)

    for case in range(0, int(cases)):
        chosen_number = int(input[int(case)])

        result = sheep_count(chosen_number)

        if case == int(cases)-1:

            output.write('Case #{case}: {result}'.format(case=case+1,
                                                           result=result)
                     )
        else:
            output.write('Case #{case}: {result}\n'.format(case=case+1,
                                                           result=result)
                     )

    input_file.close()
    output.close()

if __name__ == '__main__':
    main()