def solve(n):
  if n == 0:
    return "INSOMNIA"
  x = n
  counter = 2
  seen = ['0','1','2','3','4','5','6','7','8','9']
  while (len(seen) > 0):
    for i in str(x):
        if i in seen:
            seen.remove(i)
            if len(seen) == 0:
                break
    if len(seen) == 0:
        break
    x = counter * n
    counter += 1
  return x

# input() reads a string with a line of input, stripping the '\n' at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  print("Case #{}: {}".format(i, solve(int(input()))))
  # check out .format's specification for more formatting options
