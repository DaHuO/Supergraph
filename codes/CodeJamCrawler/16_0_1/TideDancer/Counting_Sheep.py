import numpy

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = long(input())  # read a line with a single longeger
for i in range(1, t + 1):
  x = long(input())
  x_string = str(x)
  digits_set = set(x_string)
  if(x==0):
    o = 'INSOMNIA'
  else:
    k = 2
    while(len(digits_set) < 10):
      y = x*k
      k = k + 1
      digits_set = digits_set.union(set(str(y)))
    o = str(y)

  # n, m = [long(s) for s in input().split(" ")]  # read a list of longegers, 2 in this case
  print("Case #{}: {}".format(i, o))
  # check out .format's specification for more formatting options
