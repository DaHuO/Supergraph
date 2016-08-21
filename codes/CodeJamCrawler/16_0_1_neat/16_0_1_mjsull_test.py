import sys
out_file = open(sys.argv[2], 'w')
with open(sys.argv[1]) as in_file:
    num_of_cases = int(in_file.readline().rstrip())
    for i in range(num_of_cases):
        number = int(in_file.readline().rstrip())
        if number == 0:
            out_file.write('Case #' + str(i+1) + ': INSOMNIA\n')
            continue
        the_set = set()
        for j in str(number):
            the_set.add(j)
        multiplier = 1
        while len(the_set) < 10:
            multiplier += 1
            new_number = number * multiplier
            for j in str(new_number):
                the_set.add(j)
        out_file.write('Case #' + str(i+1) + ': ' + str(number * multiplier) + '\n')
