# Problem A. Counting Sheep

with open('A-large.in', 'rb') as _f:
    with open('output1.txt', 'wb') as _file:
        no_of_test_cases = int(_f.readline())
        for i in xrange(1, no_of_test_cases + 1):
            input_string = _f.readline()
            result_string = input_string[0]
            input_string = input_string[1:]
            for char in input_string:
                if char >= result_string[0]:
                    result_string = char + result_string
                else:
                    result_string  += char

            _file.write("Case #" + str(i) + ": " + result_string)
