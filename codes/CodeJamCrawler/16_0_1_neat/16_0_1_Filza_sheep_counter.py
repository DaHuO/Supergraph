def sheep_counter(N):
    numset = set()
    remaining_num = N
    i = 1

    if N == 0 :
        return "INSOMNIA"

    while len(numset) < 10:
        if remaining_num < 10:
            i += 1
            remaining_num = N * i   

        num_counted = remaining_num % 10
        numset.add(num_counted)
        remaining_num /= 10

        
        if remaining_num < 10:
            numset.add(remaining_num)

    return N * i




# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

num_testcases = int(raw_input())  # read a line with a single integer
for i in xrange(1, num_testcases + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, sheep_counter(n))



  # n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case




