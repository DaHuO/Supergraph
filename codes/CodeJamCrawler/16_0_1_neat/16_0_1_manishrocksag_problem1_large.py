# Problem A. Counting Sheep

with open('A-large.in', 'rb') as _f:
    with open('output5.txt', 'wb') as _file:
        no_of_test_cases = int(_f.readline())

        for i in xrange(1, no_of_test_cases + 1):
            digit_set = set()
            input_number = int(_f.readline())

            if int(input_number) == 0:
                _file.write("Case #" + str(i) + ": " + "INSOMNIA" + "\n")
                continue

            generated_number = input_number
            for iter in xrange(2, 1000000):
                generated_number = str(generated_number)
                for digit in generated_number:
                    digit_set.add(digit)

                if len(digit_set) == 10:
                    _file.write("Case #" + str(i) + ": " + str(generated_number) + "\n")
                    break
                else:
                    generated_number = int(input_number) * iter

                    if generated_number == 0:
                        digit_set.add('0')
                        if len(digit_set) == 10:
                            _file.write("Case #" + str(i) + ": " + str(generated_number) + "\n")
                            break
                        else:
                            _file.write("Case #" + str(i) + ": " + "INSOMNIA" + "\n")
                            break

