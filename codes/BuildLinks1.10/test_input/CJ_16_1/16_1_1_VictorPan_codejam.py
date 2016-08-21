def solve(s):
  answer = s[0]
  maxSeen = answer
  for letter in s[1:]:
      if letter >= maxSeen:
          maxSeen = letter
          answer = letter + answer
      else:
          answer = answer + letter
  return answer

# input() reads a string with a line of input, stripping the '\n' at the end.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s = input()
    print("Case #{}: {}".format(i, solve(s)))
    # check out .format's specification for more formatting options
