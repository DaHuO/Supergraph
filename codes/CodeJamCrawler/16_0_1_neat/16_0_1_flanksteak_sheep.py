import sys

def do_test_case(fd):
    tokens = fd.readline()

    num = int(tokens)
    ans = 0
    curr_num = num

    while True:
        for c in str(curr_num):
            ans |= (1 << int(c))

# sys.stdout.write("%d -> %s -> %d\n" % (curr_num, c, ans))
            
            if ans == 1023:
                print curr_num
                return

        last_num = curr_num
        curr_num += num

        if last_num == curr_num:
            print "INSOMNIA"
            return


##################
file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    sys.stdout.write("Case #%d: " % (i))
    do_test_case(fd)

