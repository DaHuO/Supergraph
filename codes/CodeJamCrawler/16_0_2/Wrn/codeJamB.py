def flip( s, k ):
    if s.count('+') == len(s) :
        return k
    else:
        return flip(s.lstrip(s[0]),k+1)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s = raw_input()
  k = flip( s, 0 )
  print "Case #{}: {}".format(i, k)

  # check out .format's specification for more formatting options
