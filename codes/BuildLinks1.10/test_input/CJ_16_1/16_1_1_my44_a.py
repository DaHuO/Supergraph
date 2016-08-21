t = int(input())
strings = [0 for i in range(t)]
for i in range(t):
  strings[i] = input()

outstrs = []
for string in strings:
  outstr = string[0]
  for char in string[1:]:
    if char < outstr[0]:
      outstr = outstr + char
    else:
      outstr = char + outstr
  outstrs.append(outstr)

for i in range(t):
  print("Case #{}: {}".format(i+1, outstrs[i]))
