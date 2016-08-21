def sleeper(num):
    if num==0:
        return 'INSOMNIA'
    seen=''
    current=num
    while True:
        # print "currently looking at %i"%current
        for letter in str(current):
            if letter not in seen:
                # print "I haven't seen "+letter
                seen+=letter
        if len(seen)==10:
            return current
        current+=num

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    num=raw_input()
    # print num
    result = sleeper(int(num))
    print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options