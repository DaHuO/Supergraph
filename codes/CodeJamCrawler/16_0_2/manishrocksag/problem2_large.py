# Problem B. Pancake Counting Large


def transform(x):
    if x == '-':
        return '+'
    if x == '+':
        return '-'

with open('B-large.in', 'rb') as _f:
    with open('output3.txt', 'wb') as _file:
        no_of_test_cases = int(_f.readline())

        for i in xrange(1, no_of_test_cases + 1):
            input_arr = list(_f.readline().rstrip('\n\r'))
            cost = 0
            while '-' in input_arr:
                if len(input_arr) == 1:
                    if input_arr[0] == '-':
                        cost += 1
                    break

                for index, item in enumerate(input_arr):

                    if index == 0:
                        previous_item = item
                        current_item = item
                    else:
                        previous_item = input_arr[index-1]
                        current_item = item

                    _index = index

                    if previous_item == current_item:
                        pass
                    else:
                        if index - 1 == 0:
                            input_arr[index-1] = transform(input_arr[index-1])
                            cost += 1
                            break
                        else:
                            counter = 0
                            _index = _index - 1
                            while counter <= _index:
                                input_arr[counter], input_arr[_index] = transform(input_arr[_index]), transform(input_arr[counter])
                                counter += 1
                                _index -= 1

                            cost += 1
                            break

                if '+' not in input_arr:
                    cost += 1
                    break

            _file.write("Case #" + str(i) + ": " + str(cost) + "\n")


