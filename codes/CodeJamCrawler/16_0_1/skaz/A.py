test_cases = input()

def print_result(t, result):
    print "Case #" + str(t + 1) + ": " + str(result)

def add_digits_to_set(current_number, the_set):
    for ch in str(current_number):
        the_set.add(ch)

def handle_case(t):
    N= input()
    multiplier = 1
    current = N

    used_numbers = set()

    if N == 0:
        print_result(t, "INSOMNIA")
    else:
        add_digits_to_set(N, used_numbers)

        while(len(used_numbers) is not 10):
            multiplier += 1
            current = N * multiplier
            add_digits_to_set(current, used_numbers)

        print_result(t, current)


for t in range(0, test_cases):
    handle_case(t)


