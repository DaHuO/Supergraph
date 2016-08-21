input_filename = 'A-large.in'

with open(input_filename, 'r') as infile:
    test_cases = int(infile.readline())
    for test_case in range(1, test_cases+1):
        #a, b, c = [int(x) for x in infile.readline().split()]
        string = infile.readline().strip()
        result = [string[0]]
        for letter in string[1:]:
            if letter >= result[0]:
                result = [letter] + result
            else:
                result.append(letter)

        result_str = ''.join(result)
        print('Case #{}: {}'.format(test_case, result_str))
