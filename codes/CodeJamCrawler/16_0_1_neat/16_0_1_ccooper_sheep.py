import sys

lines = sys.stdin.readlines()

line_num = 0

test_cases = int(lines[line_num])
line_num += 1

for test_case in range(0, test_cases):
    n1 = int(lines[line_num])
    line_num += 1

    if n1 == 0:
        print "Case #%d: INSOMNIA" % (test_case + 1)
        continue

    n = 0
    digits_found = [0] * 10
    while(sum(digits_found) <> 10):
        n += n1
        n_as_string = "%d" % (n)
        for i in range(0, len(n_as_string)):
            digits_found[int(n_as_string[i])] = 1
    
    print "Case #%d: %d" % (test_case + 1, n)
