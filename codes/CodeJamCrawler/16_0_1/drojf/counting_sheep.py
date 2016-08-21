import itertools

set_of_all_digits = {0,1,2,3,4,5,6,7,8,9}

def put_numbers_into_set(num, put_set):
    while(True):
        digits_except_last = (num // 10)
        last_digit = num - digits_except_last * 10
        put_set.add(last_digit)
        num = digits_except_last

        if(digits_except_last == 0):
            return

def test_number(num):
    if num == 0:
        return "INSOMNIA"

    seen_digits = set()

    for num_i in itertools.count(start=num, step=num):
        put_numbers_into_set(num_i, seen_digits)
        if seen_digits == set_of_all_digits:
            return num_i

def output_generator(input_file):
    num_cases = int(f.readline())
    for i in range(num_cases):
        case_N = int(input_file.readline())
        #print(test_number(case_N))
        result = test_number(case_N)
        yield 'Case #{}: {}\n'.format(i+1, result)


f = open('input.txt')
out_f = open('output.txt','w')

out_f.writelines(output_generator(f))

