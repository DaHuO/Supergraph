# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())
for case in xrange(1, t+1):
    n = int(raw_input())  # read a line with a single integer
    digits = ['0','1','2','3','4','5','6','7','8','9']
    for i in xrange(1, 100000):
        curr_number = n*i
        number_string = str(curr_number)
        for d in number_string:
            if d in digits:
                digits.remove(d)
                if not digits:
                    print "Case #{}: {}".format(case, curr_number)
                    break
        if not digits:
            break
    if digits:
        print "Case #{}: INSOMNIA".format(case)
