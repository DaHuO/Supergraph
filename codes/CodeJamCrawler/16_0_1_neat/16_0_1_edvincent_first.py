import copy

number_of_lines = int(raw_input())

def run_first(case_number, N):
    seen = set()
    i = 1
    times_no_diff = 0
    ret = None

    while True:
        seen_before = seen.copy()
        number = i * N
        #print 'Processing ' + str(number)

        for digit in str(number):
            seen.add(int(digit))

        if not seen.difference(seen_before):
            times_no_diff = times_no_diff + 1
        else:
            times_no_diff = 0

        if len(seen) == 10:
            ret = str(number)
        # Arbitrarily chosen...
        elif times_no_diff == 1000000:
            ret =  'INSOMNIA'

        if ret:
            return 'Case #{}: {}'.format(case_number, ret)
        else:
            i = i + 1

for line in range(1, number_of_lines + 1):
    number = int(raw_input())
    print run_first(case_number = line, N = number)
