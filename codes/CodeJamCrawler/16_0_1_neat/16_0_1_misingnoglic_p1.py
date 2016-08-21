
cases = open("A-large.in").read().splitlines()[1:]
cases = [int(x) for x in cases]
case_number = 1
for case in cases:
    if case == 0:
        answer = "INSOMNIA"
    else:
        current_iteration = 1
        counted_digits = [False for x in range(10)]
        while True:
            current_number = current_iteration*case
            digits = [int(x) for x in str(current_number)]
            for digit in digits:
                counted_digits[digit]=True

            if all(counted_digits):
                answer = str(current_number)
                break

            else:
                current_iteration+=1
    print "Case #{}: {}".format(case_number, answer)
    case_number+=1