# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
num_cases = int(raw_input())  # read a line with a single integer
for casenum in xrange(num_cases):
    n = int(raw_input())
    i = 0
    digits_seen = set()
    rounds_of_no_change = 0
    while len(digits_seen) < 10 and rounds_of_no_change <= 150:
        i = i + 1
        cur_num = n*i
        cur_digits = {d for d in str(cur_num)}
        #print "cur_num:{} cur_digits:{} digits_seen:{} rounds_of_no_change:{}".format(cur_num, cur_digits, digits_seen, rounds_of_no_change)
        new_digits_seen = digits_seen.union(cur_digits)
        if len(new_digits_seen - digits_seen) == 0:
            rounds_of_no_change = rounds_of_no_change + 1
        else:
            rounds_of_no_change = 0
        digits_seen = new_digits_seen
        
    print "Case #{}: {}".format(casenum+1, (n*i) if len(digits_seen) == 10 else "INSOMNIA")

