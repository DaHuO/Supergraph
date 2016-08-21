def resolution(first_number):
    if first_number == 0: 
        return "INSOMNIA"
    
    index = 1
    set_numbers = set()
    last_number = first_number
    while len(set_numbers) < 10:
        last_number = index * first_number
        set_numbers.update(str(last_number))
        for num_str in str(last_number):
            set_numbers.add(num_str)
        index += 1
    return last_number

if __name__ == '__main__':
    tests = int(raw_input())
    for test_case, test in enumerate(xrange(tests), 1):
        answer = resolution(int(raw_input()))
        print "Case #{}: {}".format(test_case, answer)
