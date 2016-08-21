cases = int(raw_input())
counter = 0

def check_number(case):
    for i in case:
        if i not in integers:
            integers.append(i)
    return

while (counter < cases):
    integers = []
    count_multiply = 0
    case = list(raw_input())
    if case == ['0']:
        print "Case #"+str(counter+1)+": INSOMNIA"
    else:
        initial_case = int("".join(case))
        check_number(case)
        while len(integers) < 10:
            count_multiply += 1
            case = ''.join(case)
            case = initial_case * count_multiply
            case = list(str(case))
            check_number(case)
        print "Case #"+str(counter+1)+": {}".format(initial_case * count_multiply)
    counter += 1
