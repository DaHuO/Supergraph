def do_happy(s, n):
    is_positive = True
    for x in s:
        if x == "-":
            is_positive = False
            break
    if is_positive:
        return n

    #drop last positive strings bc they're done
    length = len(s)
    for x in xrange(len(s)):
        if s[(length-x-1)] == "+":
            s = s[0:len(s)-1]
        else:
            break

    # recursive case: if first positive: seek for farthest positive from top to flip to negative
    # if first negative: seek for farhtest negative to flip
    is_first_positive = (s[0] == "+")
    if is_first_positive:
        ctr = 0
        pos = 0
        while (True and ctr < len(s)):
            if s[ctr] == "-":
                pos = ctr
                break
            ctr = ctr + 1
        new_string = s[0:pos:-1]
        rest = s[pos::]
        for x in xrange(len(new_string)):
            if new_string[x] == "+":
                new_string[x] = "-"
            else:
                new_string[x] = "+"
        return do_happy(new_string + rest, n+1)
    else:
        new_string = s[::-1]
        for x in xrange(len(new_string)):
            if new_string[x] == "+":
                new_string[x] = "-"
            else:
                new_string[x] = "+"
        return do_happy(new_string, n+1)

def do_happy_wrap(s):
    return do_happy(list(s), 0)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  x = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, do_happy_wrap(x[0]))
  # check out .format's specification for more formatting options
