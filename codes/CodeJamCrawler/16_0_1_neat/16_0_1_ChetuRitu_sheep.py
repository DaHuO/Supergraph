def sheep(num):
    mask = 0x3FF
    num_bits = 0


    if(num == 0):
        return "INSOMNIA"

    for i in xrange(1,500):
        ret = num * i
        ret_string = str(ret)

        if '0' in ret_string:
            num_bits |= 0x1
        if '1' in ret_string:
            num_bits |= 0x2
        if '2' in ret_string:
            num_bits |= 0x4
        if '3' in ret_string:
            num_bits |= 0x8
        if '4' in ret_string:
            num_bits |= 0x10
        if '5' in ret_string:
            num_bits |= 0x20
        if '6' in ret_string:
            num_bits |= 0x40
        if '7' in ret_string:
            num_bits |= 0x80
        if '8' in ret_string:
            num_bits |= 0x100
        if '9' in ret_string:
            num_bits |= 0x200
#        print ret_string

        if num_bits == mask:
            return ret

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = [int(s) for s in raw_input().split("\n")]  # read a list of integers, 2 in this case
#    print "num #{}".format(n[0])
    print "Case #{}: {}".format(i, sheep(n[0]))
#    print "end"
  # check out .format's specification for more formatting options
#num = input( "enter num:")
#print "Hello "  
#print sheep(num)

