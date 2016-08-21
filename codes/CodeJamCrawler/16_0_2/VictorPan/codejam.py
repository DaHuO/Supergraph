def solve(s):
  answer = 0
  current = None
  for c in s:
    if c == '+':
      if current == None:
          current = '+'
      elif current != c:
          answer += 1
          current = '+'
    else:
      if current == None:
          current = '-'
      elif current != c:
          answer += 1
          current = '-'

  if current == '-':
      answer += 1
  return answer

# input() reads a string with a line of input, stripping the '\n' at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s = input()
  print("Case #{}: {}".format(i, solve(s)))
  # check out .format's specification for more formatting options
