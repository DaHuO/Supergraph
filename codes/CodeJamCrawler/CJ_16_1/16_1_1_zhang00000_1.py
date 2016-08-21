def LastWord(s):
    new = s[0]
    for item in s[1:]:
        if item < new[0]:
            new = new + item
        else:
            new = item + new
    return new



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s= input()
  print("Case #{}: {}".format(i, LastWord(s)))
  # check out .format's specification for more formatting options
