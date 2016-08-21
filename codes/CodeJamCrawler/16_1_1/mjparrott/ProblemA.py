import sys

f = open(sys.argv[1], "r")

t = int(f.readline())
for i in range(t):
  s = f.readline().strip()

  new_string = s[0]
  for c in s[1:]:
    if c >= new_string[0]:
      new_string = c + new_string
    else:
      new_string = new_string + c

  print("Case #{}: {}".format(i + 1, new_string))
