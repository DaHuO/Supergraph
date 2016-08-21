test_case = 'large'

# BASIC SETUP
import cStringIO

with open('{0}.in'.format(test_case)) as f:
    lines = f.readlines()
cases = int(lines.pop(0))

output = cStringIO.StringIO()
# END BASIC SETUP

for case in xrange(cases):
    N = int(lines[case].strip())
    if N == 0:
        last_num = "INSOMNIA"
    else:
        digits_seen = set()
        for x in xrange(1,10000):
            digits_this_num = set(str(x*N))
            digits_seen.update(digits_this_num)
            if len(digits_seen) == 10:
                last_num = x*N
                break

    output_line = "Case #{0}: {1}".format(case+1, last_num)
    print output_line
    print >>output, output_line


### DEFAULT OUTPUT
with open('{0}.out'.format(test_case), 'w') as f:
    f.write(output.getvalue())
### DEFAULT OUTPUT
